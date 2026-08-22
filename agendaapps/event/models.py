from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from agendaapps.institute.models import Institution, Attendence
from agendaapps.authentication.models import User
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from django.utils import timezone


import datetime
from django.template.defaultfilters import slugify
import uuid

import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import uuid


class TypeAgenda(models.Model):
    """Tipu Ajenda"""

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )

    name_type = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Tipu Ajenda'
    )

    name_type_slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        editable=False,
        verbose_name='Tipu Ajenda Slug'
    )

    class Meta:
        verbose_name = "Tipu Ajenda"
        verbose_name_plural = "Tipu Ajenda"
        ordering = ['name_type']

    def __str__(self):
        return self.name_type

    def get_absolute_url(self):
        return reverse(
            "typeagenda_detail",
            kwargs={"uuid": self.uuid}
        )

    def save(self, *args, **kwargs):

        # Automatically generate slug from Tipu Ajenda
        self.name_type_slug = slugify(self.name_type)

        super().save(*args, **kwargs)
    
class CatAgenda(models.Model):
    """Category Agenda Model"""

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )

    name_category = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Kategoria Ajenda'
    )

    name_category_slug = models.SlugField(
        max_length=255,
        blank=True,
        unique=True,
        editable=False,
        verbose_name='Kategoria Ajenda Slug'
    )

    class Meta:
        verbose_name = "Kategoria Ajenda"
        verbose_name_plural = "Kategoria Ajenda"
        ordering = ['name_category']

    def __str__(self):
        return self.name_category

    def get_absolute_url(self):
        return reverse(
            "CatAgenda",
            kwargs={
                "name_category_slug": self.name_category_slug
            }
        )

    def save(self, *args, **kwargs):

        # Automatically create slug from category name
        self.name_category_slug = slugify(self.name_category)

        super().save(*args, **kwargs)


class AgendaRecipient(models.Model):

    name = models.CharField(
        max_length=150,
        verbose_name="Naran"
    )

    position = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Kargu"
    )

    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )

    is_default = models.BooleanField(
        default=False,
        verbose_name="Simu Ajenda Automaticamente"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Ativu"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    uuid = models.UUIDField(
            default=uuid.uuid4,
            editable=False,
            unique=True,
            db_index=True
        )

    class Meta:
        ordering = ["name"]
        verbose_name = "Agenda Recipient"
        verbose_name_plural = "Agenda Recipients"

    def __str__(self):
        return f"{self.name} - {self.email}"


class AgendaTo(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    
    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Kodigu"
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Naran"
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name

    
class Agenda(models.Model):
    """ Event model """

    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Ajenda'
    )

    title_slug = models.SlugField(
        max_length=255,
        null=False,
        unique=True,
        verbose_name='Title-Slug'
    )

    catagenda = models.ForeignKey(
        CatAgenda,
        on_delete=models.CASCADE,
        related_name="agenda",
        verbose_name="Kategoria Ajenda"
    )

    meeting_type = models.ForeignKey(
        TypeAgenda,
        on_delete=models.CASCADE,
        related_name="agenda",
        verbose_name="Tipu Ajenda"
    )

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name="agenda",
        verbose_name="Instituisaun"
    )

    start_time = models.DateTimeField(
        verbose_name="Oras Hahu"
    )

    end_time = models.DateTimeField(
        verbose_name="Oras Remata"
    )

    location = models.CharField(
        max_length=255,
        null=False,
        blank=True,
        verbose_name="Fatin"
    )

    observation = HTMLField(
        null=True,
        blank=True,
        verbose_name='OBSERVASAUN'
    )

    attachment = models.FileField(
        upload_to='agenda_files/',
        null=True,
        blank=True,
        verbose_name="Dokumentu"
    )

    recipients = models.ManyToManyField(
        "AgendaRecipient",
        blank=True,
        related_name="agendas",
        verbose_name="Receptor Email"
    )

    # =====================================================
    # CENTRAL SSO USER
    # =====================================================

    central_user_id = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Central User ID"
    )

    central_username = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Central Username"
    )

    # =====================================================
    # STATUS
    # =====================================================

    is_cancel = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Read', 'Read'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )

    # =====================================================
    # AUDIT
    # =====================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )


    class Meta:
        verbose_name_plural = "Ajenda"
        ordering = ('-start_time',)


    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse(
            "Agenda",
            kwargs={
                "title_slug": self.title_slug
            }
        )


    def save(self, *args, **kwargs):

        if not self.title_slug:

            base_slug = slugify(
                self.title
            )

            slug = base_slug
            counter = 1

            while Agenda.objects.filter(
                title_slug=slug
            ).exclude(
                pk=self.pk
            ).exists():

                slug = (
                    f"{base_slug}-{counter}"
                )

                counter += 1

            self.title_slug = slug

        super().save(
            *args,
            **kwargs
        )   
    
class AgendaDelegation(models.Model):
    
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )

    agenda = models.ForeignKey(
        Agenda,
        on_delete=models.CASCADE,
        related_name="delegations",
        verbose_name="Ajenda"
    )

    delegated_from = models.ForeignKey(
        AgendaTo,
        on_delete=models.PROTECT,
        related_name="delegations_from",
        verbose_name="Delega Husi"
    )

    delegated_to = models.ForeignKey(
        AgendaTo,
        on_delete=models.PROTECT,
        related_name="delegations_to",
        verbose_name="Delega Ba"
    )

    delegated_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Data no Oras Delegasaun"
    )

    note = models.TextField(
        null=True,
        blank=True,
        verbose_name="Nota Delegasaun"
    )

    central_user_id = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        db_index=True
    )

    central_username = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ("-delegated_at",)

    def __str__(self):
        return (
            f"{self.agenda} | "
            f"{self.delegated_from} -> "
            f"{self.delegated_to}"
        )
        
class Notification(models.Model):

    NOTIFICATION_TYPES = (
        ("AGENDA_NEW", "Ajenda Foun"),
        ("AGENDA_UPDATE", "Ajenda Atualizadu"),
        ("DELEGATION", "Delegasaun"),
        ("REMINDER", "Reminder"),
    )

    RECIPIENT_ROLES = (
        ("ajenda_user", "Ministro"),
        ("ajenda_vmn", "Vice Ministro"),
    )

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )

    recipient_role = models.CharField(
        max_length=50,
        choices=RECIPIENT_ROLES,
        db_index=True,
        verbose_name="Recipient Role"
    )

    notification_type = models.CharField(
        max_length=30,
        choices=NOTIFICATION_TYPES,
        db_index=True,
        verbose_name="Tipu Notifikasaun"
    )

    title = models.CharField(
        max_length=255,
        verbose_name="Titulu"
    )

    message = models.TextField(
        verbose_name="Mensajen"
    )

    agenda = models.ForeignKey(
        "Agenda",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notifications"
    )

    url = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    created_by_user_id = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    created_by_username = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = [
            "-created_at"
        ]

        indexes = [
            models.Index(
                fields=[
                    "recipient_role",
                    "notification_type",
                    "created_at",
                ]
            ),
        ]

        verbose_name = "Notifikasaun"
        verbose_name_plural = "Notifikasaun"

    def __str__(self):

        return (
            f"{self.title} - "
            f"{self.recipient_role}"
        )


# ============================================================
# NOTIFICATION READ
# ============================================================

class NotificationRead(models.Model):

    notification = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE,
        related_name="reads"
    )

    central_user_id = models.CharField(
        max_length=100,
        db_index=True
    )

    central_username = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    read_at = models.DateTimeField(
        default=timezone.now
    )

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "notification",
                    "central_user_id",
                ],
                name="unique_notification_read_user"
            )

        ]

        verbose_name = "Notifikasaun Le'e"
        verbose_name_plural = "Notifikasaun Le'e"

    def __str__(self):

        return (
            f"{self.notification.title} - "
            f"{self.central_username}"
        )
        
        
        
        
        
        
        
        
        
        
        


class HistAgenda(models.Model):
    """ Event model """
    id = models.IntegerField(primary_key=True)
    title = models.CharField(
        max_length=255, unique=False, verbose_name='Ajenda')
    title_slug = models.SlugField(
        max_length=255, null=False, unique=False, verbose_name='Titulu-Slug')
    catagenda = models.CharField(
        max_length=25, null=True, verbose_name="Pendente")
    institution = models.CharField(
        max_length=255, null=True, verbose_name="Kria Ajenda")
    start_time = models.DateTimeField(null=True)
    start_time_new = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True)
    end_time_new = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    location_new = models.CharField(max_length=255, null=True, blank=True)
    meeting_type = models.CharField(
        max_length=255,  blank=True, verbose_name='Tipu Enkontru')
    observation = models.TextField(null=True)
    is_cancel = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    STATUS = (
        ('Pending', 'Pending'),
        ('Read', 'Read'),
    )
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # managed = True
        verbose_name_plural = ("Historia Ajenda ")
        ordering = ('-start_time_new', )

    def __str__(self):
        return str(self.title)

    # def get_absolute_url(self):
    #     return reverse("Title", kwargs={"title_slug": self.title_slug})

    # def save(self, *args, **kwargs):  # new
    #     if not self.title_slug:
    #         self.title_slug = slugify(self.title)
    #     return super(HistAgenda, self).save(*args, **kwargs)


class RequestAgenda(models.Model):
    title = models.CharField(
        max_length=255, unique=True, verbose_name='Pedidu Ajenda:')
    title_slug = models.SlugField(
        max_length=255, null=False, unique=True, verbose_name='Titulu-Slug')
    catagenda = models.ForeignKey(
        CatAgenda, on_delete=models.CASCADE, related_name="requestagenda", verbose_name="Kategoria Ajenda:", null=True)
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name="requestagenda", verbose_name="Instituisaun:", null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    location = models.CharField(max_length=255, null=False, blank=True)
    is_active = models.BooleanField(default=False)
    STATUS = (
        ('Pending', 'Pending'),
        ('Read', 'Read'),
    )
    status = models.CharField(max_length=20, choices=STATUS, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # managed = True
        verbose_name_plural = ("Pedidu Ajenda ")
        ordering = ('-created_at', )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Title", kwargs={"title_slug": self.title_slug})

    def save(self, *args, **kwargs):  # new
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        return super(RequestAgenda, self).save(*args, **kwargs)


class Yearagenda(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(2022, datetime.date.today().year+1)]
    year = models.IntegerField(
        _('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_active = models.BooleanField(default=False)

    class Meta:
        # managed = False
        verbose_name_plural = ("Ajenda Tuir Tinan")
        ordering = ('-year', )

    def __str__(self):
        return str(self.year)


class Informative(models.Model):
    """ Event model """
    title = models.CharField(max_length=255, unique=True,
                             verbose_name='Nota Informativu')
    title_slug = models.SlugField(
        max_length=255, null=False, unique=True, verbose_name='Titulu-Slug')
    is_active = models.BooleanField(default=True)
    is_done = models.BooleanField(default=False)
    is_comment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # managed = False
        verbose_name_plural = ("Informativu")
        ordering = ('-created_at', )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Informativu", kwargs={"title_slug": self.title_slug})

    def save(self, *args, **kwargs):
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        return super(Informative, self).save(*args, **kwargs)


class CommentInformative(models.Model):
    informative = models.ForeignKey(
        Informative, on_delete=models.CASCADE, related_name='commentinformative')
    problems = models.TextField(
        null=False, blank=True, verbose_name="Problema:")
    results = models.TextField(
        null=False, blank=True, verbose_name="Rezultadu:")
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.results[:60]

  
class AgendaNotification(models.Model):

    REMINDER_1_DAY = "1_day"
    REMINDER_2_HOURS = "2_hours"

    REMINDER_CHOICES = (
        (
            REMINDER_1_DAY,
            "1 Day Before"
        ),
        (
            REMINDER_2_HOURS,
            "2 Hours Before"
        ),
    )

    agenda = models.ForeignKey(
        Agenda,
        on_delete=models.CASCADE,
        related_name="email_notifications"
    )

    recipient = models.ForeignKey(
        AgendaRecipient,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    reminder_type = models.CharField(
        max_length=20,
        choices=REMINDER_CHOICES
    )

    sent_at = models.DateTimeField(
        null=True,
        blank=True
    )

    success = models.BooleanField(
        default=False
    )

    error_message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "agenda",
                    "recipient",
                    "reminder_type",
                ],
                name="unique_agenda_email_reminder"
            )
        ]

    def __str__(self):
        return (
            f"{self.agenda.title} - "
            f"{self.recipient.name} - "
            f"{self.reminder_type}"
        )