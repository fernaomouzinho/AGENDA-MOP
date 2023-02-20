from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
import datetime


# Create your models here.

class AgendaAbstract(models.Model):
    """ Event abstract model """
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AgendaManager(models.Manager):
    """ Event manager """

    def get_all_agenda(self, user):
        agenda = Agenda.objects.filter(
            user=user, is_active=True, is_deleted=False)
        return agenda

    def get_running_agenda(self, user):
        running_agenda = Agenda.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_agenda


class Agenda(AgendaAbstract):
    """ Event model """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200, unique=True)
    title_slug = models.SlugField(max_length=255, null=False, unique=True, verbose_name='Title-Slug')
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_cancel = models.BooleanField(default=False)
    objects = AgendaManager()

    class Meta:
        # managed = False
        verbose_name_plural = ("Agenda")
        ordering = ('-start_time', )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Agenda", kwargs={"title_slug": self.title_slug})


class Yearagenda(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year+1)]
    year = models.IntegerField(
        _('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_active = models.BooleanField(default=False)

    class Meta:
        # managed = False
        verbose_name_plural = ("Agenda Year")
        ordering = ('-year', )

    def __str__(self):
        return str(self.year)


class Informative(models.Model):
    """ Event model """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="informative")
    title = models.CharField(max_length=200, unique=True)
    title_slug = models.SlugField(max_length=255, null=False, unique=True, verbose_name='Title-Slug')
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_cancel = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # managed = False
        verbose_name_plural = ("Informative")
        ordering = ('-start_time', )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Informative", kwargs={"title_slug": self.title_slug})

class CommentInformative(models.Model):
    informative = models.ForeignKey(Informative, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


   
