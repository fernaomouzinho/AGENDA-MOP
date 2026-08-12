from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from agendaapps.institute.models import Institution, Attendence
from agendaapps.authentication.models import User
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField


import datetime
from django.template.defaultfilters import slugify

class TypeAgenda(models.Model):
    """ Tipu agenda model """

    name_type = models.CharField(
        max_length=200, unique=True, verbose_name='Tipu Ajenda')
    name_type_slug = models.CharField(
        max_length=255, null=True, unique=True, verbose_name='Tipu Ajenda Slug')

    class Meta:
        # managed = True
        verbose_name_plural = ("Tipu Ajenda")

    def __str__(self):
        return str(self.name_type)

    def get_absolute_url(self):
        return reverse("TypeAgenda", kwargs={"name_type_slug": self.name_type_slug})

    def save(self, *args, **kwargs):  # new
        if not self.name_type_slug:
            self.name_type_slug = slugify(self.name_type)
        return super(TypeAgenda, self).save(*args, **kwargs)
    
class CatAgenda(models.Model):
    """ Category agenda model """

    name_category = models.CharField(
        max_length=200, unique=True, verbose_name='Kategoria Ajenda')
    name_category_slug = models.CharField(
        max_length=255, null=True, unique=True, verbose_name='Kategoria Ajenda Slug')

    class Meta:
        # managed = True
        verbose_name_plural = ("Kategoria Ajenda")

    def __str__(self):
        return str(self.name_category)

    def get_absolute_url(self):
        return reverse("CatAgenda", kwargs={"name_category_slug": self.name_category_slug})

    def save(self, *args, **kwargs):  # new
        if not self.name_category_slug:
            self.name_category_slug = slugify(self.name_category)
        return super(CatAgenda, self).save(*args, **kwargs)


class Agenda(models.Model):
    """ Event model """
    title = models.CharField(
        max_length=255, unique=True, verbose_name='Ajenda')
    title_slug = models.SlugField(
        max_length=255, null=False, unique=True, verbose_name='Title-Slug')
    catagenda = models.ForeignKey(
        CatAgenda, on_delete=models.CASCADE, related_name="agenda", verbose_name="Kategoria Ajenda")
    meeting_type = models.ForeignKey(
        TypeAgenda, on_delete=models.CASCADE, related_name="agenda", verbose_name="Tipu Ajenda")
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name="agenda", verbose_name="Instituisaun")
    start_time = models.DateTimeField(verbose_name="Oras Hahu")
    end_time = models.DateTimeField(verbose_name="Oras Remata")
    location = models.CharField(max_length=255, null=False, blank=True, verbose_name="Fatin")
    observation = HTMLField(null=True, blank=True, verbose_name='OBSERVASAUN')
    attachment = models.FileField(
        upload_to='agenda_files/', 
        null=True,
        blank=True,
        verbose_name="Dokumentu"
    )

    is_cancel = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    STATUS = (
        ('Pending', 'Pending'),
        ('Read', 'Read'),
    )
    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # managed = True
        verbose_name_plural = ("Ajenda")
        ordering = ('-start_time', )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Agenda", kwargs={"title_slug": self.title_slug})

    def save(self, *args, **kwargs):  # new
        # if not self.title_slug:
        #     self.title_slug = slugify(self.title)
        # return super(Agenda, self).save(*args, **kwargs)
        if not self.title_slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Agenda.objects.filter(title_slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.title_slug = slug
        super().save(*args, **kwargs)
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


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
