from django.contrib import admin
from .models import Agenda, CommentAgenda, Yearagenda

# Register your models here.


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    model = Agenda
    list_display = [
        "id",
        "title",
        "user",
        "is_active",
        "is_deleted",
        "start_time",
        "end_time",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]
    prepopulated_fields = {"title_slug": (
        "title",)}  # new


@admin.register(CommentAgenda)
class CommentEventAdmin(admin.ModelAdmin):
    model = CommentAgenda
    list_display = [
        "id",
        "agenda",
        "user",
    ]
    list_filter = ["agenda"]
    search_fields = ["agenda"]


@admin.register(Yearagenda)
class YeareventsAdmin(admin.ModelAdmin):
    model = Yearagenda
    list_display = [
        "id",
        "year",
        "is_active",
    ]
    list_filter = ["year"]
    search_fields = ["year"]
