from django.db import models
from agendaapps.authentication.models import User
import uuid

# Create your models here.


class Institution(models.Model):
    name_institution = models.CharField(
        max_length=255, null=True, verbose_name="Naran Instituisaun:")
    uuid = models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                unique=True,
                db_index=True
            )

    class Meta:
        # managed = False
        verbose_name_plural = ("Instituisaun Nebe Konvida")

    def __str__(self):
        return str(self.name_institution)


class Attendence(models.Model):
    name_attendence = models.CharField(
        max_length=255, null=True, verbose_name="Atendente")

    class Meta:
        # managed = False
        verbose_name_plural = ("Atendente")

    def __str__(self):
        return str(self.name_attendence)


class unitADN(models.Model):
    name_unit = models.CharField(
        max_length=255, null=True, verbose_name="Unit Of:")
    abreviation = models.CharField(
        max_length=10, null=True, verbose_name="Abreviation:")

    class Meta:
        # managed = False
        verbose_name_plural = ("Unit ADN")

    def __str__(self):
        return str(self.name_unit)


class DepartmentADN(models.Model):
    unitadn = models.ForeignKey(unitADN, on_delete=models.CASCADE,
                                null=True, related_name="unitadn", verbose_name="Unit Of:")
    name_department = models.CharField(
        max_length=255, null=True, verbose_name="Unit Of:")

    class Meta:
        # managed = False
        verbose_name_plural = ("Department ADN")

    def __str__(self):
        return str(self.name_department)
