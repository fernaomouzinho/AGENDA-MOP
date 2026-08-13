from django.db.models.signals import post_save
from django.dispatch import receiver

from agendaapps.event.models import (
    Agenda,
    AgendaRecipient,
)


@receiver(post_save, sender=Agenda)
def assign_default_recipients(
    sender,
    instance,
    created,
    **kwargs
):

    if not created:
        return

    default_recipients = (
        AgendaRecipient.objects
        .filter(
            is_active=True,
            is_default=True
        )
    )

    instance.recipients.add(
        *default_recipients
    )