from django.db import models
from eventapps.authentication.models import User

# Create your models here.


class Institution(models.Model):
    name_institution = models.CharField(
        max_length=255, null=True, verbose_name="Institution Name:")

    class Meta:
        # managed = False
        verbose_name_plural = ("Institution Invited")

    def __str__(self):
        return str(self.name_institution)


class Attendence(models.Model):
    name_attendence = models.CharField(
        max_length=255, null=True, verbose_name="Attendant")

    class Meta:
        # managed = False
        verbose_name_plural = ("Attendant")

    def __str__(self):
        return str(self.name_attendence)
