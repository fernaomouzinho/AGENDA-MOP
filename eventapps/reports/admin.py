from django.contrib import admin
from eventapps.reports.models import Semestral, Trimestral, Mensual

# Register your models here.
class SemestralAdmin(admin.ModelAdmin):
    list_display = ['id',  'name']
    prepopulated_fields = {"name": ("name_slug",)}  # new
admin.site.register(Semestral, SemestralAdmin)

class TrimestralAdmin(admin.ModelAdmin):
    list_display = ['id',  'name']
    prepopulated_fields = {"name": ("name_slug",)}  # new
admin.site.register(Trimestral, TrimestralAdmin)

class MensualAdmin(admin.ModelAdmin):
    list_display = ['id',  'name']
    prepopulated_fields = {"name": ("name_slug",)}  # new
admin.site.register(Mensual, MensualAdmin)