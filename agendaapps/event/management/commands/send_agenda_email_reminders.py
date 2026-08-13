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
# REMINDER CONFIGURATION
# ============================================================

REMINDERS = [

    # --------------------------------------------------------
    # 1 DAY REMINDER
    #
    # Send between:
    # 24 hours before
    # and
    # 23 hours 30 minutes before
    # --------------------------------------------------------

    {
        "type": AgendaNotification.REMINDER_1_DAY,

        "max_remaining": timedelta(days=1),

        "min_remaining": timedelta(
            hours=23,
            minutes=30
        ),

        "text": "loron 1",
    },


    # --------------------------------------------------------
    # 2 HOURS REMINDER
    #
    # Send between:
    # 2 hours before
    # and
    # 1 hour 30 minutes before
    # --------------------------------------------------------

    {
        "type": AgendaNotification.REMINDER_2_HOURS,

        "max_remaining": timedelta(hours=2),

        "min_remaining": timedelta(
            hours=1,
            minutes=30
        ),

        "text": "oras 2",
    },

]


class Command(BaseCommand):

    help = (
        "Send automatic Agenda email reminders."
    )


    def add_arguments(self, parser):

        parser.add_argument(
            "--test",
            type=int,
            help="Send test email for Agenda ID."
        )


    def handle(self, *args, **options):

        # ====================================================
        # TEST MODE
        # ====================================================

        test_agenda_id = options.get("test")

        if test_agenda_id:

            self.run_test(
                test_agenda_id
            )

            return


        # ====================================================
        # NORMAL AUTOMATIC MODE
        # ====================================================

        now = timezone.now()

        local_now = timezone.localtime(now)


        self.stdout.write("")
        self.stdout.write(
            "=" * 70
        )

        self.stdout.write(
            "Checking Agenda email reminders at: "
            f"{local_now.strftime('%d/%m/%Y %H:%M:%S')}"
        )

        self.stdout.write(
            "=" * 70
        )


        # ====================================================
        # Only need to search approximately 1 day ahead
        # ====================================================

        maximum_time = (
            now
            + timedelta(days=1)
        )


        agendas = (
            Agenda.objects
            .filter(
                start_time__gt=now,
                start_time__lte=maximum_time,
                is_active=True,
                is_cancel=False,
            )
            .prefetch_related(
                "recipients"
            )
            .order_by(
                "start_time"
            )
        )


        self.stdout.write(
            f"Agenda found: {agendas.count()}"
        )


        total_sent = 0
        total_failed = 0


        # ====================================================
        # CHECK EACH AGENDA
        # ====================================================

        for agenda in agendas:

            remaining = (
                agenda.start_time - now
            )

            local_start = timezone.localtime(
                agenda.start_time
            )


            self.stdout.write("")
            self.stdout.write(
                "-" * 70
            )

            self.stdout.write(
                f"Checking Agenda: {agenda.title}"
            )

            self.stdout.write(
                f"Agenda ID: {agenda.id}"
            )

            self.stdout.write(
                "Start Time: "
                f"{local_start.strftime('%d/%m/%Y %H:%M')}"
            )

            self.stdout.write(
                f"Remaining: {remaining}"
            )


            # =================================================
            # ACTIVE RECIPIENTS
            # =================================================

            recipients = (
                agenda
                .recipients
                .filter(
                    is_active=True
                )
            )


            self.stdout.write(
                f"Active recipients: {recipients.count()}"
            )


            if not recipients.exists():

                self.stdout.write(
                    "No active recipients. Skipping."
                )

                continue


            matched_any_reminder = False


            # =================================================
            # CHECK REMINDER RANGES
            # =================================================

            for reminder in REMINDERS:

                max_remaining = (
                    reminder["max_remaining"]
                )

                min_remaining = (
                    reminder["min_remaining"]
                )


                self.stdout.write(
                    "Checking reminder: "
                    f"{reminder['text']} | "
                    f"Range: "
                    f"{min_remaining} - "
                    f"{max_remaining}"
                )


                # =============================================
                # IMPORTANT RANGE CHECK
                #
                # Example for 2 hours:
                #
                # 1:30 <= remaining <= 2:00
                # =============================================

                if not (
                    min_remaining
                    <= remaining
                    <= max_remaining
                ):

                    continue


                matched_any_reminder = True


                self.stdout.write(
                    self.style.SUCCESS(
                        "Reminder MATCHED: "
                        f"{reminder['text']}"
                    )
                )


                # =============================================
                # SEND TO EACH RECIPIENT
                # =============================================

                for recipient in recipients:


                    # =========================================
                    # CHECK IF ALREADY SENT
                    # =========================================

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
                                "Already sent: "
                                f"{recipient.name} "
                                f"({recipient.email})"
                            )
                        )

                        continue


                    # =========================================
                    # CREATE / GET NOTIFICATION RECORD
                    # =========================================

                    notification, created = (
                        AgendaNotification.objects
                        .get_or_create(
                            agenda=agenda,
                            recipient=recipient,
                            reminder_type=reminder["type"],
                        )
                    )


                    # =========================================
                    # SEND EMAIL
                    # =========================================

                    try:

                        self.stdout.write(
                            "Sending email to: "
                            f"{recipient.name} "
                            f"<{recipient.email}>"
                        )


                        send_agenda_email(
                            agenda=agenda,
                            recipient=recipient,
                            reminder_text=reminder["text"],
                        )


                        # =====================================
                        # SUCCESS
                        # =====================================

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


                        total_sent += 1


                        self.stdout.write(
                            self.style.SUCCESS(
                                "Email sent successfully: "
                                f"{recipient.name}"
                            )
                        )


                    except Exception as exc:

                        # =====================================
                        # FAILED
                        # =====================================

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


                        total_failed += 1


                        self.stderr.write(
                            self.style.ERROR(
                                "Email failed: "
                                f"{recipient.name} | "
                                f"{exc}"
                            )
                        )


            # =================================================
            # NO REMINDER MATCH
            # =================================================

            if not matched_any_reminder:

                self.stdout.write(
                    "Not currently inside a reminder range."
                )


        # ====================================================
        # FINISHED
        # ====================================================

        self.stdout.write("")
        self.stdout.write(
            "=" * 70
        )

        self.stdout.write(
            f"Completed | "
            f"Sent: {total_sent} | "
            f"Failed: {total_failed}"
        )

        self.stdout.write(
            "=" * 70
        )


    # ========================================================
    # TEST MODE
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
            "AGENDA EMAIL TEST MODE"
        )

        self.stdout.write(
            "=" * 70
        )


        try:

            agenda = (
                Agenda.objects
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
                    f"Agenda ID {agenda_id} "
                    "does not exist."
                )
            )

            return


        recipients = (
            agenda
            .recipients
            .filter(
                is_active=True
            )
        )


        self.stdout.write(
            f"Agenda: {agenda.title}"
        )

        self.stdout.write(
            f"Agenda ID: {agenda.id}"
        )

        self.stdout.write(
            f"Active recipients: "
            f"{recipients.count()}"
        )


        if not recipients.exists():

            self.stdout.write(
                "No active recipients."
            )

            return


        # ====================================================
        # SEND TEST
        # ====================================================

        for recipient in recipients:

            self.stdout.write("")
            self.stdout.write(
                "Sending test email to:"
            )

            self.stdout.write(
                f"Name : {recipient.name}"
            )

            self.stdout.write(
                f"Email: {recipient.email}"
            )


            try:

                send_agenda_email(
                    agenda=agenda,
                    recipient=recipient,
                    reminder_text="TESTE",
                )


                self.stdout.write(
                    self.style.SUCCESS(
                        "Test email sent successfully."
                    )
                )


            except Exception as exc:

                self.stderr.write(
                    self.style.ERROR(
                        f"Test email failed: {exc}"
                    )
                )


        self.stdout.write("")
        self.stdout.write(
            "=" * 70
        )