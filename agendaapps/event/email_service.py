from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone


def send_agenda_email(
    agenda,
    recipient,
    reminder_text
):

    # Konverte oras ba timezone lokal
    local_start = timezone.localtime(
        agenda.start_time
    )

    local_end = timezone.localtime(
        agenda.end_time
    )

    # Asuntu email
    subject = (
        f"Notifikasaun Ajenda-MOP: {agenda.title}"
    )

    # Dadus atu haruka ba template HTML
    context = {
        "agenda": agenda,
        "recipient": recipient,
        "reminder_text": reminder_text,
        "local_start": local_start,
        "local_end": local_end,
    }

    # Versaun textu simples
    text_body = (
        f"Prezado/a {recipient.name},\n\n"

        f"Ne'e mak notifikasaun automátika husi Sistema Ajenda "
        f"atu fó-hanoin kona-ba ajenda tuir mai:\n\n"

        f"Ajenda: {agenda.title}\n"
        f"Data: {local_start.strftime('%d/%m/%Y')}\n"
        f"Oras Hahu: {local_start.strftime('%H:%M')}\n"
        f"Oras Remata: {local_end.strftime('%H:%M')}\n"
        f"Fatin: {agenda.location}\n"
        f"Instituisaun: {agenda.institution}\n\n"

        f"Ajenda ne'e sei hahú iha {reminder_text} oin mai.\n\n"

        f"Ho respeitu,\n"
        f"Sistema Ajenda\n"
        f"Ministériu Obras Públikas"
    )

    # Versaun HTML
    html_body = render_to_string(
        "event/email/agenda_reminder.html",
        context
    )

    # Kria email
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[
            recipient.email
        ],
    )

    # Tau HTML ba email
    email.attach_alternative(
        html_body,
        "text/html"
    )

    # Haruka email
    return email.send(
        fail_silently=False
    )