from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Agenda
from agendaapps.institute.models import Attendence
from .services import build_agenda_message, generate_whatsapp_link


@receiver(post_save, sender=Agenda)
def send_agenda_whatsapp(sender, instance, created, **kwargs):
    if created:
        message = build_agenda_message(instance)

        attendees = Attendence.objects.filter(agenda=instance)

        for att in attendees:
            # make sure user has phone_number
            phone = getattr( "phone_number", None)

            if phone:
                link = generate_whatsapp_link(phone, message)

                print(f"Send WhatsApp to {phone}: {link}")
                
                print("SIGNAL LOADED")