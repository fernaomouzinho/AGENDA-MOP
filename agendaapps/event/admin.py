
from django.contrib import admin
from .models import TypeAgenda, CatAgenda, AgendaTo, Agenda, AgendaDelegation, RequestAgenda, HistAgenda, Yearagenda, Informative, CommentInformative


class TypeAgendaAdmin(admin.ModelAdmin):
    list_display = ['id',  'name_type']


admin.site.register(TypeAgenda, TypeAgendaAdmin)

class CatAgendaAdmin(admin.ModelAdmin):
    list_display = ['id',  'name_category']


admin.site.register(CatAgenda, CatAgendaAdmin)


# ==========================================
# Existing Agenda Admin
# ==========================================

class AgendaAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'title',
        'start_time',
        'end_time',
        'location',
        'observation',
        'is_cancel',
        'is_active',
        'status',
    ]

    prepopulated_fields = {
        "title_slug": ("title",)
    }

    list_filter = [
        'is_cancel',
        'is_active',
        'status',
        'catagenda',
        'meeting_type',
        'institution',
    ]

    search_fields = [
        'title',
        'location',
    ]


admin.site.register(
    Agenda,
    AgendaAdmin
)

# ============================================================
# AGENDA TO
# ============================================================

@admin.register(AgendaTo)
class AgendaToAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "uuid",
        "name",
        "is_active",
    ]

    list_filter = [
        "is_active",
    ]

    search_fields = [
        "name"
    ]

    ordering = [
        "id",
    ]


# ============================================================
# AGENDA DELEGATION INLINE
# ============================================================

class AgendaDelegationInline(admin.TabularInline):
    model = AgendaDelegation

    extra = 0

    fields = [
        "delegated_from",
        "delegated_to",
        "delegated_at",
        "note",
        "central_username",
        "is_active",
    ]

    readonly_fields = [
        "central_username",
    ]



class HistAgendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_time', 'end_time',
                    'start_time_new', 'end_time_new', 'location_new']


admin.site.register(HistAgenda, HistAgendaAdmin)


class YearAgendaAdmin(admin.ModelAdmin):
    list_display = ['year',  'is_active',]


admin.site.register(Yearagenda, YearAgendaAdmin)


class RequestedAgendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    prepopulated_fields = {"title": ("title_slug",)}  # new


admin.site.register(RequestAgenda, RequestedAgendaAdmin)


class InformativeAdmin(admin.ModelAdmin):
    list_display = ['id',  'title']
    prepopulated_fields = {"title": ("title_slug",)}  # new


admin.site.register(Informative, InformativeAdmin)


class CommentInformativeAdmin(admin.ModelAdmin):
    list_display = ['id',  'informative', 'problems',
                    'results', 'created_on', 'is_active']


admin.site.register(CommentInformative, CommentInformativeAdmin)
