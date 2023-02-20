from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from eventapps.institute.models import Institution, Attendence
from django.contrib.auth.models import User

import datetime
from django.template.defaultfilters import slugify

class CatAgenda(models.Model):
    """ Category agenda model """

    name_category = models.CharField(max_length=200, unique=True, verbose_name='Category Agenda')
   
    class Meta:
        #managed = True
        verbose_name_plural = ("Category Agenda")

    def __str__(self):
        return str(self.name_category)


class Agenda(models.Model):
    """ Event model """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agenda")
    title = models.CharField(max_length=200, unique=True, verbose_name='Agenda')
    title_slug = models.SlugField(max_length=255, null=False, unique=True, verbose_name='Title-Slug')
    catagenda=models.ForeignKey(CatAgenda, on_delete=models.CASCADE, related_name="agenda", verbose_name="Category Agenda")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="agenda", verbose_name="Institution")
    attendence = models.ForeignKey(Attendence, on_delete=models.CASCADE, related_name="agenda", verbose_name='Attendant')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255, null=False, blank=True)
    observation = models.TextField(null=True, blank=True)
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
        #managed = True
        verbose_name_plural = ("Agenda")
        ordering = ('-start_time', )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Agenda", kwargs={"title_slug": self.title_slug})
    
    def save(self, *args, **kwargs):  # new
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        return super(Agenda, self).save(*args, **kwargs)
    

class HistAgenda(models.Model):
    """ Event model """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="histagenda")
    title = models.CharField(max_length=200, unique=True, verbose_name='Agenda')
    title_slug = models.SlugField(max_length=255, null=False, unique=True, verbose_name='Title-Slug')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="histagenda", verbose_name="Institution")
    attendence = models.ForeignKey(Attendence, on_delete=models.CASCADE, related_name="histagenda", verbose_name='Attendant')
    start_time = models.DateTimeField(null=True)
    start_time_new = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True)
    end_time_new = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    location_new = models.CharField(max_length=255, null=True, blank=True)
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
        #managed = True
        verbose_name_plural = ("Agenda History ")
        ordering = ('-start_time_new', )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Title", kwargs={"title_slug": self.title_slug})
    
    def save(self, *args, **kwargs):  # new
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        return super(HistAgenda, self).save(*args, **kwargs)



class Yearagenda(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(2022, datetime.date.today().year+1)]
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="informative")
    title = models.CharField(max_length=255, unique=True, verbose_name='Nota Informative')
    title_slug = models.SlugField(max_length=255, null=False, unique=True, verbose_name='Title-Slug')
    is_active = models.BooleanField(default=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # managed = False
        verbose_name_plural = ("Informative")
        ordering = ('-created_at', )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Informative", kwargs={"title_slug": self.title_slug})
    

    def save(self, *args, **kwargs):  
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        return super(Informative, self).save(*args, **kwargs)

class CommentInformative(models.Model):
    informative = models.ForeignKey(Informative, on_delete=models.CASCADE, related_name='commentinformative')
    comment = models.TextField(verbose_name="Add New Comment")
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
   
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment[:60]
    


   
