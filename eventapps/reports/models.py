from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.template.defaultfilters import slugify

# Create your models here.

class Semestral(models.Model):
    name = models.CharField(max_length=100, null=True)
    name_slug = models.SlugField(max_length=100, null=True, unique=True, verbose_name='Name-Slug')

    class Meta:
        # managed = True
        verbose_name_plural = ("Semetral")

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("Semestral", kwargs={"name_slug": self.name_slug})

    def save(self, *args, **kwargs):  # new
        if not self.name_slug:
            self.name_slug = slugify(self.name)
        return super(Semestral, self).save(*args, **kwargs)

class Trimestral(models.Model):
    name = models.CharField(max_length=100, null=True)
    name_slug = models.SlugField(max_length=100, null=True, unique=True, verbose_name='Name-Slug')

    class Meta:
        # managed = True
        verbose_name_plural = ("Trimestral")

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("Trimestral", kwargs={"name_slug": self.name_slug})

    def save(self, *args, **kwargs):  # new
        if not self.name_slug:
            self.name_slug = slugify(self.name)
        return super(Trimestral, self).save(*args, **kwargs)
    
class Mensual(models.Model):
    name = models.CharField(max_length=100, null=True)
    name_slug = models.SlugField(max_length=100, null=True, unique=True, verbose_name='Name-Slug')

    class Meta:
        # managed = True
        verbose_name_plural = ("Mensual")

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("Mensual", kwargs={"name_slug": self.name_slug})

    def save(self, *args, **kwargs):  # new
        if not self.name_slug:
            self.name_slug = slugify(self.name)
        return super(Mensual, self).save(*args, **kwargs)