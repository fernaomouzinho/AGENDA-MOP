from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from agendaapps.event.models import (
    Agenda,
    AgendaNotification,
)

from agendaapps.event.email_service import (
    send_agenda_email,
)


# ============================================================
# CONFIGURATION
# ============================================================

# Windows Task Scheduler will run every 5 minutes.
#
# We use a 10 minute matching window for a little
# extra protection against small scheduling delays.
REMINDER_WINDOW = timedelta(
    minutes=10
)


REMINDERS = [

    # ========================================================
    # 1 DAY BEFORE
    # ========================================================

    {
        "type": AgendaNotification.REMINDER_1_DAY,
        "target": timedelta(days=1),
        "text": "1 day",
    },

    # ========================================================
    # 2 HOURS BEFORE
    # ========================================================

    {
        "type": AgendaNotification.REMINDER_2_HOURS,
        "target": timedelta(hours=2),
        "text": "2 hours",
    },

]


class Command(BaseCommand):

    help = (
        "Send automatic Agenda email reminders "
        "1 day and 2 hours before meetings."
    )

    # ========================================================
    # TEST ARGUMENT
    # ========================================================

    def add_arguments(
        self,
        parser
    ):

        parser.add_argument(
            "--test",
            type=int,
            help=(
                "Agenda ID to send immediately "
                "for testing."
            ),
        )

    # ========================================================
    # MAIN
    # ========================================================

    def handle(
        self,
        *args,
        **options
    ):

        # ====================================================
        # TEST MODE
        # ====================================================

        test_agenda_id = options.get(
            "test"
        )

        if test_agenda_id:

            self.run_test(
                test_agenda_id
            )

            return

        # ====================================================
        # CURRENT TIME
        # ====================================================

        now = timezone.now()

        local_now = timezone.localtime(
            now
        )

        self.stdout.write("")

        self.stdout.write(
            "=" * 70
        )

        self.stdout.write(
            f"Checking Agenda email reminders at: "
            f"{local_now.strftime('%d/%m/%Y %H:%M:%S')}"
        )

        self.stdout.write(
            "=" * 70
        )

        # ====================================================
        # QUERY AGENDA
        #
        # Maximum reminder is 1 day.
        # ====================================================

        maximum_time = (
            now
            + timedelta(days=1)
            + REMINDER_WINDOW
        )

        agendas = (
            Agenda.objects
            .filter(
                start_time__gt=now,
                start_time__lte=maximum_time,
                is_active=True,
                is_cancel=False,
            )
            .select_related(
                "institution",
                "catagenda",
                "meeting_type",
            )
            .prefetch_related(
                "recipients"
            )
            .order_by(
                "start_time"
            )
        )

        self.stdout.write(
            f"Agenda found: "
            f"{agendas.count()}"
        )

        total_sent = 0
        total_failed = 0

        # ====================================================
        # EACH AGENDA
        # ====================================================

        for agenda in agendas:

            remaining = (
                agenda.start_time
                - now
            )

            local_start = (
                timezone.localtime(
                    agenda.start_time
                )
            )

            self.stdout.write("")

            self.stdout.write(
                "-" * 70
            )

            self.stdout.write(
                f"Checking Agenda: "
                f"{agenda.title}"
            )

            self.stdout.write(
                f"Agenda ID: "
                f"{agenda.id}"
            )

            self.stdout.write(
                f"Start Time: "
                f"{local_start.strftime('%d/%m/%Y %H:%M')}"
            )

            self.stdout.write(
                f"Remaining: "
                f"{remaining}"
            )

            # =================================================
            # RECIPIENTS
            # =================================================

            recipients = (
                agenda
                .recipients
                .filter(
                    is_active=True
                )
            )

            self.stdout.write(
                f"Active recipients: "
                f"{recipients.count()}"
            )

            if not recipients.exists():

                self.stdout.write(
                    self.style.WARNING(
                        "No active email recipients."
                    )
                )

                continue

            reminder_found = False

            # =================================================
            # CHECK 1 DAY / 2 HOURS
            # =================================================

            for reminder in REMINDERS:

                target = reminder[
                    "target"
                ]

                lower_bound = (
                    target
                    - REMINDER_WINDOW
                )

                upper_bound = (
                    target
                )

                self.stdout.write(
                    f"Checking reminder: "
                    f"{reminder['text']} "
                    f"| target={target}"
                )

                if not (
                    lower_bound
                    <= remaining
                    <= upper_bound
                ):

                    continue

                reminder_found = True

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Reminder matched: "
                        f"{reminder['text']}"
                    )
                )

                # =============================================
                # EACH RECIPIENT
                # =============================================

                for recipient in recipients:

                    result = (
                        self.send_reminder(
                            agenda=agenda,
                            recipient=recipient,
                            reminder=reminder,
                        )
                    )

                    if result == "sent":
                        total_sent += 1

                    elif result == "failed":
                        total_failed += 1

            if not reminder_found:

                self.stdout.write(
                    "Not currently inside the "
                    "1-day or 2-hour reminder window."
                )

        # ====================================================
        # FINISH
        # ====================================================

        self.stdout.write("")

        self.stdout.write(
            "=" * 70
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Completed | "
                f"Sent: {total_sent} | "
                f"Failed: {total_failed}"
            )
        )

        self.stdout.write(
            "=" * 70
        )

        self.stdout.write("")

    # ========================================================
    # SEND REAL REMINDER
    # ========================================================

    def send_reminder(
        self,
        agenda,
        recipient,
        reminder,
    ):

        # ====================================================
        # SAFETY CHECK
        # ====================================================

        if agenda.is_cancel:

            return "cancelled"

        if not agenda.is_active:

            return "inactive"

        if not recipient.is_active:

            return "inactive"

        # ====================================================
        # ALREADY SENT?
        # ====================================================

        already_sent = (
            AgendaNotification.objects
            .filter(
                agenda=agenda,
                recipient=recipient,
                reminder_type=reminder["type"],
                success=True,
            )
            .exists()
        )

        if already_sent:

            self.stdout.write(
                self.style.WARNING(
                    f"Already sent: "
                    f"{recipient.name} "
                    f"({reminder['text']})"
                )
            )

            return "already_sent"

        # ====================================================
        # CREATE / GET NOTIFICATION
        # ====================================================

        notification, created = (
            AgendaNotification.objects
            .get_or_create(
                agenda=agenda,
                recipient=recipient,
                reminder_type=reminder["type"],
            )
        )

        # ====================================================
        # SEND
        # ====================================================

        self.stdout.write(
            f"Sending email to: "
            f"{recipient.name} "
            f"<{recipient.email}>"
        )

        try:

            result = send_agenda_email(
                agenda=agenda,
                recipient=recipient,
                reminder_text=reminder["text"],
            )

            # Django normally returns 1
            # when one email is sent.

            if result != 1:

                raise Exception(
                    f"Email backend returned {result}"
                )

            notification.success = True

            notification.sent_at = (
                timezone.now()
            )

            notification.error_message = ""

            notification.save(
                update_fields=[
                    "success",
                    "sent_at",
                    "error_message",
                ]
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Email sent successfully "
                    f"to {recipient.email}"
                )
            )

            return "sent"

        except Exception as exc:

            notification.success = False

            notification.error_message = (
                str(exc)
            )

            notification.save(
                update_fields=[
                    "success",
                    "error_message",
                ]
            )

            self.stderr.write(
                self.style.ERROR(
                    f"Email failed for "
                    f"{recipient.email}: "
                    f"{exc}"
                )
            )

            return "failed"

    # ========================================================
    # TEST MODE
    #
    # Example:
    # python manage.py send_agenda_email_reminders --test 16
    #
    # Does NOT create real reminder history.
    # ========================================================

    def run_test(
        self,
        agenda_id
    ):

        self.stdout.write("")

        self.stdout.write(
            "=" * 70
        )

        self.stdout.write(
            self.style.WARNING(
                "AGENDA EMAIL TEST MODE"
            )
        )

        self.stdout.write(
            "=" * 70
        )

        # ====================================================
        # FIND AGENDA
        # ====================================================

        try:

            agenda = (
                Agenda.objects
                .select_related(
                    "institution",
                    "catagenda",
                    "meeting_type",
                )
                .prefetch_related(
                    "recipients"
                )
                .get(
                    pk=agenda_id
                )
            )

        except Agenda.DoesNotExist:

            self.stderr.write(
                self.style.ERROR(
                    f"Agenda ID "
                    f"{agenda_id} not found."
                )
            )

            return

        # ====================================================
        # RECIPIENTS
        # ====================================================

        recipients = (
            agenda
            .recipients
            .filter(
                is_active=True
            )
        )

        self.stdout.write(
            f"Agenda: "
            f"{agenda.title}"
        )

        self.stdout.write(
            f"Agenda ID: "
            f"{agenda.id}"
        )

        self.stdout.write(
            f"Active recipients: "
            f"{recipients.count()}"
        )

        if not recipients.exists():

            self.stdout.write(
                self.style.WARNING(
                    "No active recipients."
                )
            )

            return

        # ====================================================
        # SEND TEST
        # ====================================================

        for recipient in recipients:

            self.stdout.write("")

            self.stdout.write(
                f"Sending test email to:"
            )

            self.stdout.write(
                f"Name : "
                f"{recipient.name}"
            )

            self.stdout.write(
                f"Email: "
                f"{recipient.email}"
            )

            try:

                result = send_agenda_email(
                    agenda=agenda,
                    recipient=recipient,
                    reminder_text=(
                        "TEST MESSAGE"
                    ),
                )

                if result == 1:

                    self.stdout.write(
                        self.style.SUCCESS(
                            "Test email sent "
                            "successfully."
                        )
                    )

                else:

                    self.stdout.write(
                        self.style.WARNING(
                            f"Email backend "
                            f"returned {result}"
                        )
                    )

            except Exception as exc:

                self.stderr.write(
                    self.style.ERROR(
                        f"Test email failed: "
                        f"{exc}"
                    )
                )

        self.stdout.write("")

        self.stdout.write(
            "=" * 70
        )