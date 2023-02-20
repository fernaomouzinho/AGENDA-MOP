
from django.contrib import admin
from .models import CatAgenda, Agenda, HistAgenda, Yearagenda, Informative, CommentInformative

class CatAgendaAdmin(admin.ModelAdmin):
    list_display = ['id',  'name_category']
   
admin.site.register(CatAgenda, CatAgendaAdmin)


class AgendaAdmin(admin.ModelAdmin):
    list_display = ['id',  'title', 'start_time','end_time', 'location', 'observation']
    prepopulated_fields = {"title": ("title_slug",)}  # new

admin.site.register(Agenda, AgendaAdmin)

class HistAgendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_time', 'end_time', 'start_time_new','end_time_new', 'location_new']
   
admin.site.register(HistAgenda, HistAgendaAdmin)

class YearAgendaAdmin(admin.ModelAdmin):
    list_display = ['year',  'is_active',]

admin.site.register(Yearagenda, YearAgendaAdmin)



class InformativeAdmin(admin.ModelAdmin):
    list_display = ['id',  'title']
    prepopulated_fields = {"title": ("title_slug",)}  # new

admin.site.register(Informative, InformativeAdmin)


class CommentInformativeAdmin(admin.ModelAdmin):
    list_display = ['id',  'informative', 'comment','created_on', 'is_active']

admin.site.register(CommentInformative, CommentInformativeAdmin)