from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from django.urls import reverse
from django.contrib import messages
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone

from datetime import datetime
import os


from .models import (
    TypeAgenda,
    CatAgenda,
    Agenda,
    AgendaTo,
    AgendaDelegation,
    AgendaRecipient,
    RequestAgenda,
    HistAgenda,
    Informative,
    CommentInformative,
    Notification,
    NotificationRead,
)


from .form import (
    TypeAgendaForm,
    CategoryAgendaForm,
    AgendaForm,
    AgendaToForm,
    AgendaDelegationForm,
    AgendaRecipientForm,
    PostponedAgendaForm,
    CommentAgendaForm,
    RequestedAgendaForm,
    InformativeForm,
    CommentInformativeForm,
)


from agendaapps.authentication.decorators import (
    allowed_users,
)

from agenda.utils import (
    get_roles,
)


from .services import (
    notify_new_agenda,
    notify_agenda_updated,
    notify_delegation,
    get_notifications_for_roles,
)

# ============================================================
# TYPE AGENDA LIST / ADD
# ============================================================

@allowed_users(
    allowed_roles=[
        'sii_admin',
        'ajenda_admin',
        'ajenda_user'
    ]
)
def typeagenda_list(request):
    roles = get_roles(request)
    typeagendalist = TypeAgenda.objects.all().order_by(
        'name_type')

    if request.method == "POST":

        typeagendaform = TypeAgendaForm(
            request.POST
        )

        if typeagendaform.is_valid():

            name_type = (
                typeagendaform.cleaned_data
                .get('name_type', '')
                .strip()
            )

            # ---------------------------------------------
            # CHECK DUPLICATE
            # ---------------------------------------------
            duplicate = TypeAgenda.objects.filter(
                name_type__iexact=name_type
            ).exists()

            if duplicate:

                messages.warning(
                    request,
                    f'Tipu Ajenda "{name_type}" '
                    f'iha ona iha sistema.'
                )

            else:

                obj = typeagendaform.save(
                    commit=False
                )

                obj.name_type = name_type
                obj.save()

                messages.success(
                    request,
                    f'Tipu Ajenda "{name_type}" '
                    f'aumenta ho susesu.'
                )

                return redirect(
                    'typeagenda_list'
                )

        else:

            messages.error(
                request,
                'Dadus la validu. Favor verifica fila fali.'
            )

    else:

        typeagendaform = TypeAgendaForm()

    context = {
        'typeagendaform': typeagendaform,
        'typeagendalist': typeagendalist,
        'roles': roles,
    }

    return render(
        request,
        'event/typeagenda_list.html',
        context
    )



# ============================================================
# TYPE AGENDA EDIT
# ============================================================

@allowed_users(
    allowed_roles=[
        'sii_admin',
        'ajenda_admin',
        'ajenda_user'
    ]
)
def typeagenda_edit(request, uuid):

    roles = get_roles(request)

    single_typeagenda = get_object_or_404(
        TypeAgenda,
        uuid=uuid
    )

    typeagendalist = TypeAgenda.objects.all().order_by(
        'name_type'
    )

    if request.method == "POST":

        typeagendaform = TypeAgendaForm(
            request.POST,
            instance=single_typeagenda
        )

        if typeagendaform.is_valid():

            name_type = (
                typeagendaform.cleaned_data
                .get('name_type', '')
                .strip()
            )

            duplicate = (
                TypeAgenda.objects
                .filter(
                    name_type__iexact=name_type
                )
                .exclude(
                    uuid=single_typeagenda.uuid
                )
                .exists()
            )

            if duplicate:

                messages.warning(
                    request,
                    f'Tipu Ajenda "{name_type}" '
                    f'iha ona iha sistema.'
                )

            else:

                obj = typeagendaform.save(
                    commit=False
                )

                obj.name_type = name_type

                # save() automatically updates slug
                obj.save()

                messages.success(
                    request,
                    f'Tipu Ajenda "{name_type}" '
                    f'atualiza ho susesu.'
                )

                return redirect(
                    'typeagenda_list'
                )

        else:

            messages.error(
                request,
                'Dadus la validu. Favor verifica fila fali.'
            )

    else:

        typeagendaform = TypeAgendaForm(
            instance=single_typeagenda
        )

    context = {
        'single_typeagenda': single_typeagenda,
        'typeagendaform': typeagendaform,
        'typeagendalist': typeagendalist,
        'roles': roles,
    }

    return render(
        request,
        'event/typeagenda_edit.html',
        context
    )
    
    
# ============================================================
# TYPE AGENDA DELETE
# ============================================================

@allowed_users(
    allowed_roles=[
        'sii_admin',
        'ajenda_admin'
    ]
)
def typeagenda_delete(request, uuid):

    roles = get_roles(request)

    single_typeagenda = get_object_or_404(
        TypeAgenda,
        uuid=uuid
    )

    # related_name="agenda" in Agenda.meeting_type
    usage_count = single_typeagenda.agenda.count()

    if request.method == "POST":

        if usage_count > 0:

            messages.error(
                request,
                f'Tipu Ajenda "{single_typeagenda.name_type}" '
                f'la bele hamos tanba uza hela iha '
                f'{usage_count} Ajenda.'
            )

            return redirect(
                'typeagenda_list'
            )

        name_type = single_typeagenda.name_type

        single_typeagenda.delete()

        messages.success(
            request,
            f'Tipu Ajenda "{name_type}" '
            f'hamos ho susesu.'
        )

        return redirect(
            'typeagenda_list'
        )

    context = {
        'single_typeagenda': single_typeagenda,
        'usage_count': usage_count,
        'roles': roles,
    }

    return render(
        request,
        'event/typeagenda_delete.html',
        context
    )
    
    
# Create your views here.
# ======================================== Category Agenda Add ================================================================
@allowed_users(
    allowed_roles=[
        'sii_admin',
        'ajenda_admin',
        'ajenda_user'
    ]
)
def categoryagenda_list(request):

    roles = get_roles(request)

    catagendalist = CatAgenda.objects.all().order_by(
        'name_category'
    )

    if request.method == "POST":

        categoryagendaform = CategoryAgendaForm(
            request.POST
        )

        if categoryagendaform.is_valid():

            name_category = (
                categoryagendaform.cleaned_data
                .get('name_category', '')
                .strip()
            )

            # ==========================================
            # CHECK DUPLICATE
            # ==========================================
            duplicate = CatAgenda.objects.filter(
                name_category__iexact=name_category
            ).exists()

            if duplicate:

                messages.warning(
                    request,
                    f'Kategoria Ajenda "{name_category}" '
                    f'iha ona iha sistema.'
                )

            else:

                categoryagendaform.save()

                messages.success(
                    request,
                    f'Kategoria Ajenda "{name_category}" '
                    f'rai ho susesu.'
                )

                return redirect(
                    'categoryagenda_list'
                )

        else:

            messages.error(
                request,
                "Dadus la validu. Favor verifica fila fali."
            )

    else:

        categoryagendaform = CategoryAgendaForm()


    context = {
        'categoryagendaform': categoryagendaform,
        'catagendalist': catagendalist,
        'roles': roles,
    }

    return render(
        request,
        'event/category_agenda_list.html',
        context
    )

# ============================================= Category Agenda Edit ================================================================

@allowed_users(
    allowed_roles=[
        'sii_admin',
        'ajenda_admin',
        'ajenda_user'
    ]
)
def categoryagenda_edit(request, uuid):

    roles = get_roles(request)

    single_categoryagenda = get_object_or_404(
        CatAgenda,
        uuid=uuid
    )

    catagendalist = CatAgenda.objects.all().order_by(
        'name_category'
    )

    if request.method == "POST":

        categoryagendaform = CategoryAgendaForm(
            request.POST,
            request.FILES,
            instance=single_categoryagenda
        )

        if categoryagendaform.is_valid():

            name_category = (
                categoryagendaform.cleaned_data
                .get('name_category', '')
                .strip()
            )

            # ==========================================
            # CHECK DUPLICATE
            # Exclude current category
            # ==========================================
            duplicate = (
                CatAgenda.objects
                .filter(
                    name_category__iexact=name_category
                )
                .exclude(
                    pk=single_categoryagenda.pk
                )
                .exists()
            )

            if duplicate:

                messages.warning(
                    request,
                    f'Kategoria Ajenda "{name_category}" '
                    f'iha ona iha sistema.'
                )

            else:

                categoryagendaform.save()

                messages.success(
                    request,
                    f'Kategoria Ajenda "{name_category}" '
                    f'atualiza ho susesu.'
                )

                return redirect(
                    'categoryagenda_list'
                )

        else:

            messages.error(
                request,
                "Dadus la validu. Favor verifica fila fali."
            )

    else:

        categoryagendaform = CategoryAgendaForm(
            instance=single_categoryagenda
        )


    context = {
        'single_categoryagenda': single_categoryagenda,
        'catagendalist': catagendalist,
        'categoryagendaform': categoryagendaform,
        'roles': roles,
    }

    return render(
        request,
        'event/category_agenda_edit.html',
        context
    )


@allowed_users(allowed_roles=['sii_admin', 'ajenda_admin'])
def categoryagenda_delete(request, uuid):

    single_categoryagenda = get_object_or_404(
        CatAgenda,
        uuid=uuid
    )

    # Check whether this category is already used by Agenda
    agenda_count = single_categoryagenda.agenda.count()

    if request.method == "POST":

        # Do not delete category if Agenda is using it
        if agenda_count > 0:

            messages.error(
                request,
                "Kategoria Ajenda ida-ne'e la bele hamos "
                "tanba iha Ajenda ne'ebé uza hela kategoria ida-ne'e."
            )

            return redirect('categoryagenda_list')

        # Save name before deleting
        category_name = single_categoryagenda.name_category

        # Delete
        single_categoryagenda.delete()

        messages.success(
            request,
            f'Kategoria Ajenda "{category_name}" hamos ho susesu.'
        )

        return redirect('categoryagenda_list')


    context = {
        'single_categoryagenda': single_categoryagenda,
        'agenda_count': agenda_count,
    }

    return render(
        request,
        'event/category_agenda_delete.html',
        context
    )

# ======================================== List All Agenda ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def agenda_list(request):
    roles = get_roles(request)
    context = {
        'roles':roles
    }
    return render(request, 'event/agenda_list.html', context)

# ============================================= Agenda Add ================================================================
@allowed_users(
    allowed_roles=[
        "sii_admin",
        "ajenda_admin",
        "ajenda_user",
    ]
)
def agenda_add(request):

    # ==========================================
    # CURRENT DATETIME
    # ==========================================
    current_datetime = timezone.now()


    if request.method == "POST":

        form = AgendaForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            agenda = form.save(
                commit=False
            )


           # ==========================================
            # SSO USER WHO CREATED THE AGENDA
            # ==========================================

            central_user_id = (
                getattr(
                    request,
                    "portal_user_id",
                    None
                )
                or
                request.session.get(
                    "agenda_user_id"
                )
            )

            central_username = (
                getattr(
                    request,
                    "portal_user",
                    None
                )
                or
                request.session.get(
                    "agenda_user"
                )
            )

            agenda.central_user_id = (
                str(central_user_id)
                if central_user_id
                else ""
            )

            agenda.central_username = (
                central_username
                or ""
            )


            # ==========================================
            # SET AGENDA STATUS
            # ==========================================

            if (
                agenda.start_time
                >=
                current_datetime
            ):

                agenda.status = (
                    "Pending"
                )


            elif (
                agenda.start_time
                <=
                current_datetime
                and
                agenda.end_time
                >=
                current_datetime
            ):

                agenda.status = (
                    "Read"
                )


            elif (
                agenda.end_time
                <
                current_datetime
            ):

                agenda.status = (
                    "Read"
                )


            # ==========================================
            # SAVE AGENDA
            # ==========================================

            agenda.save()


            # ==========================================
            # SAVE MANY-TO-MANY RECIPIENTS
            # ==========================================

            form.save_m2m()
            
            notify_new_agenda(
                request,
                agenda
            )


            # ==========================================
            # CREATE AGENDA HISTORY
            # ==========================================

            ha = HistAgenda(

                id=agenda.id,

                title=agenda.title,

                title_slug=agenda.title_slug,

                catagenda=(
                    agenda.catagenda.name_category
                ),

                institution=(
                    agenda.institution.name_institution
                ),

                start_time=(
                    agenda.start_time
                ),

                start_time_new=(
                    agenda.start_time
                ),

                end_time=(
                    agenda.end_time
                ),

                end_time_new=(
                    agenda.end_time
                ),

                location=(
                    agenda.location
                ),

                location_new=(
                    agenda.location
                ),

                meeting_type=(
                    agenda.meeting_type.name_type
                ),

                observation=(
                    agenda.observation
                ),

                is_cancel=(
                    agenda.is_cancel
                ),

                is_active=(
                    agenda.is_active
                ),

                status=(
                    agenda.status
                ),

                created_at=(
                    agenda.created_at
                ),

                updated_at=(
                    agenda.updated_at
                ),
            )


            ha.save()


            # ==========================================
            # SUCCESS MESSAGE
            # ==========================================

            messages.success(
                request,
                "Ajenda rejista ho susesu."
            )


            return redirect(
                "agenda_list"
            )


        else:

            # ==========================================
            # INVALID FORM
            # ==========================================

            print(
                "Error: AgendaForm is invalid"
            )

            print(
                form.errors
            )


            messages.error(
                request,
                (
                    "Ajenda la konsege rejista. "
                    "Favor verifica dadus."
                )
            )


    else:

        form = AgendaForm()


    # ==============================================
    # CONTEXT
    # ==============================================

    context = {

        "agendaform":
            form,
    }


    return render(
        request,
        "event/agenda_add.html",
        context
    )
@allowed_users(
    allowed_roles=[
        "sii_admin",
        "ajenda_admin",
        "ajenda_user",
    ]
)
def agenda_edit(request, uuid):

    # =====================================================
    # GET AGENDA
    # =====================================================

    single_agenda = get_object_or_404(
        Agenda,
        uuid=uuid
    )


    current_datetime = (
        timezone.now()
    )


    # =====================================================
    # POST
    # =====================================================

    if request.method == "POST":

        agendaform = AgendaForm(
            request.POST,
            request.FILES,
            instance=single_agenda
        )


        if agendaform.is_valid():

            # =============================================
            # DO NOT SAVE DIRECTLY YET
            # =============================================

            agenda = agendaform.save(
                commit=False
            )


            # =============================================
            # IMPORTANT
            #
            # central_user_id
            # central_username
            #
            # remain the ORIGINAL creator.
            #
            # We do not overwrite them during edit.
            # =============================================


            # =============================================
            # UPDATE STATUS
            # =============================================

            if (
                agenda.start_time
                >
                current_datetime
            ):

                agenda.status = (
                    "Pending"
                )


            elif (
                agenda.start_time
                <=
                current_datetime
                and
                agenda.end_time
                >=
                current_datetime
            ):

                agenda.status = (
                    "Read"
                )


            elif (
                agenda.end_time
                <
                current_datetime
            ):

                agenda.status = (
                    "Read"
                )


            # =============================================
            # SAVE AGENDA
            # =============================================

            agenda.save()


            # =============================================
            # SAVE MANY TO MANY
            #
            # recipients
            # =============================================

            agendaform.save_m2m()


            # =============================================
            # CREATE UPDATE NOTIFICATION
            #
            # If agenda is delegated:
            #     -> ajenda_vmn
            #
            # If not delegated:
            #     -> ajenda_user
            # =============================================

            notify_agenda_updated(
                request,
                agenda
            )


            # =============================================
            # SUCCESS
            # =============================================

            messages.success(
                request,
                "Ajenda atualiza ho susesu."
            )


            return redirect(
                "agenda_list"
            )


        # =================================================
        # INVALID FORM
        # =================================================

        else:

            print(
                "AGENDA EDIT FORM ERROR:"
            )

            print(
                agendaform.errors
            )


            messages.error(
                request,
                (
                    "Ajenda la konsege atualiza. "
                    "Favor verifica dadus no koko fali."
                )
            )


    # =====================================================
    # GET
    # =====================================================

    else:

        agendaform = AgendaForm(
            instance=single_agenda
        )


    # =====================================================
    # CONTEXT
    # =====================================================

    context = {

        "single_agenda":
            single_agenda,

        "agendaform":
            agendaform,
    }


    return render(
        request,
        "event/agenda_edit.html",
        context
    )
# ============================================= Agenda Delete ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def agenda_delete(request, uuid):

    single_agenda = get_object_or_404(
        Agenda,
        uuid=uuid
    )

    if request.method == "POST":

        title = single_agenda.title

        single_agenda.delete()

        messages.success(
            request,
            f'Ajenda "{title}" hamos ho susesu.'
        )

        return redirect(
            "agenda_list"
        )

    context = {
        "single_agenda": single_agenda,
    }

    return render(
        request,
        "event/agenda_delete.html",
        context
    )


# ============================================================
# AGENDA TO LIST / ADD
# ============================================================
@allowed_users(
    allowed_roles=[
        'sii_admin',
        'ajenda_admin',
        'ajenda_user'
    ]
)
def agendato_list(request):

    roles = get_roles(request)

    agendatolist = AgendaTo.objects.all().order_by('name')

    if request.method == "POST":

        agendatoform = AgendaToForm(
            request.POST
        )

        if agendatoform.is_valid():

            name = (
                agendatoform.cleaned_data
                .get('name', '')
                .strip()
            )

           
            # =============================================
            # DUPLICATE NAME
            # =============================================
            name_duplicate = AgendaTo.objects.filter(
                name__iexact=name
            ).exists()

            if name_duplicate:

                messages.warning(
                    request,
                    f'Ajenda Ba "{name}" iha ona iha sistema.'
                )

            else:

                obj = agendatoform.save(
                    commit=False
                )

                obj.name = name

                obj.save()

                messages.success(
                    request,
                    f'Ajenda Ba "{name}" aumenta ho susesu.'
                )

                return redirect(
                    'agendato_list'
                )

        else:

            messages.error(
                request,
                "Dadus la validu. Favor verifica fila fali."
            )

    else:

        agendatoform = AgendaToForm()


    context = {
        'agendatoform': agendatoform,
        'agendatolist': agendatolist,
        'roles': roles,
    }

    return render(
        request,
        'event/agendato_list.html',
        context
    )
    
    
    # ============================================================
# AGENDA TO EDIT
# ============================================================

@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def agendato_edit(request, uuid):
    roles = get_roles(request)
    single_agendato = get_object_or_404(AgendaTo,uuid=uuid)
    agendatolist = AgendaTo.objects.all().order_by('name')
    if request.method == "POST":
        agendatoform = AgendaToForm(request.POST,instance=single_agendato)
        if agendatoform.is_valid():
            name = (agendatoform.cleaned_data.get('name', '').strip())
            
            # =============================================
            # CHECK DUPLICATE NAME
            # =============================================
            name_duplicate = (
                AgendaTo.objects
                .filter(
                    name__iexact=name
                )
                .exclude(
                    pk=single_agendato.pk
                )
                .exists()
            )

            if name_duplicate:

                messages.warning(
                    request,
                    f'Ajenda Ba "{name}" iha ona iha sistema.'
                )

            else:

                obj = agendatoform.save(
                    commit=False
                )

            
                obj.name = name

                obj.save()

                messages.success(
                    request,
                    f'Ajenda Ba "{name}" atualiza ho susesu.'
                )

                return redirect(
                    'agendato_list'
                )

        else:

            messages.error(
                request,
                "Dadus la validu. Favor verifica fila fali."
            )

    else:

        agendatoform = AgendaToForm(
            instance=single_agendato
        )


    context = {
        'single_agendato': single_agendato,
        'agendatoform': agendatoform,
        'agendatolist': agendatolist,
        'roles': roles,
    }

    return render(
        request,
        'event/agendato_edit.html',
        context
    )
    
# ============================================================
# AGENDA TO DELETE
# ============================================================
@allowed_users(
    allowed_roles=[
        'sii_admin',
        'ajenda_admin'
    ]
)
def agendato_delete(request, uuid):

    roles = get_roles(request)

    single_agendato = get_object_or_404(
        AgendaTo,
        uuid=uuid
    )

    # Check whether this AgendaTo is already used
    delegation_from_count = (
        single_agendato
        .delegations_from
        .count()
    )

    delegation_to_count = (
        single_agendato
        .delegations_to
        .count()
    )

    usage_count = (
        delegation_from_count
        + delegation_to_count
    )

    if request.method == "POST":

        # ==========================================
        # PROTECT USED DATA
        # ==========================================
        if usage_count > 0:

            messages.error(
                request,
                f'Ajenda Ba "{single_agendato.name}" '
                f'la bele hamos tanba uza hela iha '
                f'{usage_count} delegasaun.'
            )

            return redirect(
                'agendato_list'
            )

        name = single_agendato.name

        single_agendato.delete()

        messages.success(
            request,
            f'Ajenda Ba "{name}" hamos ho susesu.'
        )

        return redirect(
            'agendato_list'
        )


    context = {
        'single_agendato': single_agendato,
        'delegation_from_count': delegation_from_count,
        'delegation_to_count': delegation_to_count,
        'usage_count': usage_count,
        'roles': roles,
    }

    return render(
        request,
        'event/agendato_delete.html',
        context
    )

@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user','ajenda_vmn'])
def agenda_delegation_list(request):

    roles = get_roles(request)
    

    now = timezone.now()
    delegation_list = list(
        AgendaDelegation.objects
        .select_related(
            'agenda',
            'agenda__catagenda',
            'agenda__meeting_type',
            'agenda__institution',
            'delegated_from',
            'delegated_to'
        )
        .order_by('-agenda__start_time')
    )


    # =====================================================
    # COUNTERS
    # =====================================================
    total_count = 0
    upcoming_count = 0
    running_count = 0
    concluded_count = 0


    # =====================================================
    # NEXT DELEGATED MEETING
    # =====================================================
    next_delegation = None


    # =====================================================
    # CALENDAR EVENTS
    # =====================================================
    calendar_events = []


    # =====================================================
    # PROCESS DELEGATION
    # =====================================================
    for obj in delegation_list:

        total_count += 1

        agenda = obj.agenda


        # =================================================
        # UPCOMING
        # =================================================
        if now < agenda.start_time:

            obj.meeting_status = 'Upcoming'
            obj.meeting_status_label = 'TUIR MAI'

            upcoming_count += 1


            # Find nearest upcoming delegated meeting
            if (
                next_delegation is None
                or
                agenda.start_time
                <
                next_delegation.agenda.start_time
            ):

                next_delegation = obj


        # =================================================
        # RUNNING
        # =================================================
        elif (
            agenda.start_time
            <=
            now
            <=
            agenda.end_time
        ):

            obj.meeting_status = 'Running'
            obj.meeting_status_label = 'LAO HELA'

            running_count += 1


        # =================================================
        # CONCLUDED
        # =================================================
        else:

            obj.meeting_status = 'Concluded'
            obj.meeting_status_label = 'KONKLUIDU'

            concluded_count += 1


        # =================================================
        # CALENDAR
        # =================================================
        calendar_events.append({

            'id':
                str(obj.uuid),

            'title':
                agenda.title,

            'start':
                agenda.start_time.isoformat(),

            'end':
                agenda.end_time.isoformat(),

            'url':
                reverse(
                    'agenda_delegation_detail',
                    kwargs={
                        'uuid': obj.uuid
                    }
                ),

            'status':
                obj.meeting_status,

            'status_label':
                obj.meeting_status_label,

            'delegated_from':
                obj.delegated_from.name,

            'delegated_to':
                obj.delegated_to.name,

            'location':
                agenda.location or '',

            'institution':
                (
                    str(agenda.institution)
                    if agenda.institution
                    else ''
                ),

            'note':
                obj.note or '',
        })


    context = {

        'delegation_list':
            delegation_list,

        'total_count':
            total_count,

        'upcoming_count':
            upcoming_count,

        'running_count':
            running_count,

        'concluded_count':
            concluded_count,


        # NEXT MEETING
        'next_delegation':
            next_delegation,


        # CALENDAR
        'calendar_events':
            calendar_events,

        'roles':
            roles,
    }


    return render(
        request,
        'event/agenda_delegation_list.html',
        context
    )
    
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user','ajenda_vmn'])
def agenda_delegation_detail(request, uuid):

    roles = get_roles(request)

    delegation = get_object_or_404(
        AgendaDelegation.objects.select_related(
            'agenda',
            'delegated_from',
            'delegated_to',
            'agenda__catagenda',
            'agenda__meeting_type',
            'agenda__institution'
        ),
        uuid=uuid
    )

    context = {
        'delegation': delegation,
        'roles': roles,
    }

    return render(
        request,
        'event/agenda_delegation_detail.html',
        context
    )



# ================================================= Completed Agenda ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def completedAgenda_list(request):
    context = {
    }
    return render(request, 'event/completed_agenda.html', context)


# ================================================= Concluded Agenda ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def concludedAgenda_list(request):
    context = {
    }
    return render(request, 'event/concluded_agenda.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def concludedAgenda_list_detail(request, title_slug):
    single_agenda = Agenda.objects.get(title_slug=title_slug)
    all_agenda = Agenda.objects.all()

    context = {
        'single_agenda': single_agenda, 'all_agenda': all_agenda,
    }
    return render(request, 'event/concluded_agenda_detail.html', context)

# ======================================== Canceled ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def canceledAgenda_list(request):
    context = {
    }
    return render(request, 'event/canceled_agenda.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def canceledAgenda_list_detail(request, title_slug):
    single_agenda = Agenda.objects.get(title_slug=title_slug)
    all_agenda = Agenda.objects.all()

    context = {
        'single_agenda': single_agenda, 'all_agenda': all_agenda,
    }
    return render(request, 'event/canceled_agenda_detail.html', context)

# ========================================= Running ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def runningAgenda_list(request):
    current_datetime = datetime.now()
    context = {
        'current_datetime': current_datetime
    }
    return render(request, 'event/running_agenda.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def runningAgenda_list_detail(request, title_slug):
    context = {
    }
    return render(request, 'event/running_agenda_detail.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def runningagenda_change(request, pk):

    if request.method == 'POST':
        change_time = request.POST.get('minute')
        ag = Agenda.objects.get(id=pk)
        dt_object = datetime.strptime(change_time, "%d/%m/%Y %H:%M:%S")
        ag.end_time = dt_object
        ag.save()
    return redirect('runningAgenda_list')


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def runningagenda_stop(request, pk):
    ag = Agenda.objects.get(id=pk)
    current_datetime = datetime.now()
    ag.end_time = current_datetime
    ag.save()
    return redirect('runningAgenda_list')

# ======================================== Upcoming ============================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def upcomingAgenda_list(request):
    context = {
    }
    return render(request, 'event/upcoming_agenda.html', context)



@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user','ajenda_vmn'])
def upcomingAgenda_list_detail(request,title_slug):

    # ================================================================
    # GET AGENDA
    # ================================================================
    roles = get_roles(request)

    single_agenda = get_object_or_404(
        Agenda,
        title_slug=title_slug
    )

    # ================================================================
    # ALL AGENDA
    # ================================================================

    all_agenda = (
        Agenda.objects
        .all()
    )


    # ================================================================
    # CURRENT ACTIVE DELEGATION
    # ================================================================

    active_delegation = (
        AgendaDelegation.objects
        .filter(
            agenda=single_agenda,
            is_active=True
        )
        .select_related(
            "delegated_from",
            "delegated_to"
        )
        .order_by(
            "-delegated_at"
        )
        .first()
    )
    
     # =====================================================
    # CAN DELEGATE?
    #
    # TRUE only when:
    # 1. Agenda has no active delegation
    # 2. Current user is NOT Vice Minister
    # =====================================================
    can_delegate = (
        active_delegation is None
        and
        "ajenda_vmn" not in roles
    )


    # ================================================================
    # DELEGATION HISTORY
    # ================================================================

    delegation_history = (
        AgendaDelegation.objects
        .filter(
            agenda=single_agenda
        )
        .select_related(
            "delegated_from",
            "delegated_to"
        )
        .order_by(
            "-delegated_at"
        )
    )


    # ================================================================
    # POST
    # ================================================================

    if request.method == "POST":
        
         # ========================================================
    # ROLE SECURITY
    # ========================================================

        if "ajenda_vmn" in roles:

            messages.error(
                request,
                "Vice Ministro la iha permisaun atu halo delegasaun."
            )

            return redirect(
                "upcomingAgenda_list_detail",
                title_slug=single_agenda.title_slug
            )

        # ------------------------------------------------------------
        # FIRST CHECK:
        # IF ACTIVE DELEGATION ALREADY EXISTS, REJECT
        # ------------------------------------------------------------

        if (
            AgendaDelegation.objects
            .filter(
                agenda=single_agenda,
                is_active=True
            )
            .exists()
        ):

            messages.warning(
                request,
                (
                    "Ajenda ida-ne'e delega ona. "
                    "La bele aumenta delegasaun foun."
                )
            )

            return redirect(
                "upcomingAgenda_list_detail",
                title_slug=single_agenda.title_slug
            )


        # ------------------------------------------------------------
        # FORM
        # ------------------------------------------------------------

        delegation_form = (
            AgendaDelegationForm(
                request.POST
            )
        )


        # ------------------------------------------------------------
        # VALID FORM
        # ------------------------------------------------------------

        if delegation_form.is_valid():

            delegated_to = (
                delegation_form
                .cleaned_data[
                    "delegated_to"
                ]
            )

            note = (
                delegation_form
                .cleaned_data
                .get(
                    "note"
                )
            )


            # ========================================================
            # TRANSACTION
            # ========================================================

            with transaction.atomic():

                # ----------------------------------------------------
                # LOCK AGENDA ROW
                #
                # This helps prevent two simultaneous requests from
                # creating two delegations for the same agenda.
                # ----------------------------------------------------

                locked_agenda = (
                    Agenda.objects
                    .select_for_update()
                    .get(
                        pk=single_agenda.pk
                    )
                )


                # ----------------------------------------------------
                # SECOND CHECK INSIDE TRANSACTION
                # ----------------------------------------------------

                active_exists = (
                    AgendaDelegation.objects
                    .filter(
                        agenda=locked_agenda,
                        is_active=True
                    )
                    .exists()
                )


                if active_exists:

                    messages.warning(
                        request,
                        (
                            "Ajenda ida-ne'e delega ona. "
                            "Delegasaun foun la bele regista."
                        )
                    )

                    return redirect(
                        "upcomingAgenda_list_detail",
                        title_slug=(
                            single_agenda.title_slug
                        )
                    )


                # ----------------------------------------------------
                # MINISTER
                # ----------------------------------------------------

                minister = get_object_or_404(
                    AgendaTo,
                    code="MN",
                    is_active=True
                )


                # ----------------------------------------------------
                # CREATE DELEGATION
                # ----------------------------------------------------

                delegation = ( AgendaDelegation.objects.create(

                    agenda=
                        locked_agenda,

                    delegated_from=
                        minister,

                    delegated_to=
                        delegated_to,

                    delegated_at=
                        timezone.now(),

                    note=
                        note,

                    central_user_id=str(
                        getattr(
                            request,
                            "portal_user_id",
                            None
                        )
                        or
                        request.session.get(
                            "agenda_user_id",
                            ""
                        )
                    ),

                    central_username=(
                        getattr(
                            request,
                            "portal_user",
                            None
                        )
                        or
                        request.session.get(
                            "agenda_user",
                            ""
                        )
                    ),

                    is_active=
                        True
                )
                )
                notify_delegation(
                    request,
                    delegation
                )


            # ========================================================
            # SUCCESS
            # ========================================================

            messages.success(
                request,
                (
                    "Ajenda delega ho susesu. "
                    "Ajenda ida-ne'e agora iha "
                    "delegasaun ativu."
                )
            )


            return redirect(
                "agenda_delegation_list"
            )


        # ------------------------------------------------------------
        # INVALID FORM
        # ------------------------------------------------------------

        else:

            messages.error(
                request,
                (
                    "Delegasaun la konsege regista. "
                    "Favor verifica dadus no koko fali."
                )
            )


    # ================================================================
    # GET
    # ================================================================

    else:

        # ------------------------------------------------------------
        # FORM ONLY NEEDED WHEN THERE IS NO ACTIVE DELEGATION
        # ------------------------------------------------------------

        if can_delegate:

            delegation_form = (
                AgendaDelegationForm()
            )

        else:

            delegation_form = None


    # ================================================================
    # CONTEXT
    # ================================================================

    context = {

        "single_agenda":
            single_agenda,

        "all_agenda":
            all_agenda,

        "delegation_form":
            delegation_form,

        "active_delegation":
            active_delegation,

        "delegation_history":
            delegation_history,

        # Useful explicit flag
         "can_delegate":
            can_delegate,

        "roles":
            roles,
    }


    # ================================================================
    # RENDER
    # ================================================================

    return render(
        request,
        "event/upcoming_agenda_detail.html",
        context
    )


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def upcomingAgenda_edit(request, pk):
    single_agenda = Agenda.objects.get(id=pk)
    context = {
        'single_agenda': single_agenda,
    }
    return render(request, 'event/upcoming_agenda_edit.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin'])
def upcomingAgenda_delete(request, pk):

    single_agenda = Agenda.objects.get(id=pk)
    single_agenda.delete()
    messages.success(request, ("Dadus hamos ona"))
    return redirect('upcoming_view')


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def upcomingAgenda_cancel(request, pk):
    single_agenda = Agenda.objects.get(id=pk)
    single_agenda.is_cancel = "True"
    single_agenda.save()
    return redirect('canceledAgenda_list')

@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def upcomingAgenda_read(request):
    all_agenda = Agenda.objects.all()
    for a in all_agenda:
        if a.status == 'Pending':
            a.status = "Read"
            a.save()
    return redirect('upcomingAgenda_list')


# ======================================== Postpone ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def postponeAgenda_list(request, pk):

    if request.method == "POST":
        single_agenda = Agenda.objects.get(pk=pk)
        postponedagendaform = PostponedAgendaForm(
            request.POST, request.FILES, instance=single_agenda)
        if postponedagendaform.is_valid():
            postponedagendaform.save()
            sgl_agenda = Agenda.objects.get(pk=single_agenda.id)
            sgl_hagenda = HistAgenda.objects.get(pk=single_agenda.id)
            sgl_hagenda.start_time_new = sgl_agenda.start_time
            sgl_hagenda.end_time_new = sgl_agenda.end_time
            sgl_hagenda.save()

        messages.success(request, ("Data changed succesfully"))
        return redirect('upcomingAgenda_list')

    else:
        single_agenda = Agenda.objects.get(pk=pk)
        postponedagendaform = PostponedAgendaForm(instance=single_agenda)

        context = {
            'single_agenda': single_agenda,
            'postponedagendaform': postponedagendaform,
        }

    return render(request, 'event/postponed_agenda.html', context)


# ============================================= Comment Conclude Agenda Add ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def commentCoAgenda_add(request, pk):

    # ==========================================
    # GET AGENDA
    # ==========================================
    single_agenda = get_object_or_404(
        Agenda,
        pk=pk
    )

    if request.method == "POST":

        commentagendaform = CommentAgendaForm(
            request.POST,
            request.FILES,
            instance=single_agenda
        )

        if commentagendaform.is_valid():

            # ==========================================
            # 1. SAVE COMMENT TO AGENDA
            # ==========================================
            agenda = commentagendaform.save()

            print("====================================")
            print("AGENDA SAVED")
            print("Agenda ID:", agenda.pk)
            print("Observation:", agenda.observation)
            print("====================================")


            # ==========================================
            # 2. FIND HISTAGENDA
            # ==========================================

            # First try using same ID
            hist_agenda = HistAgenda.objects.filter(
                pk=agenda.pk
            ).first()


            # If history ID is different,
            # try title_slug
            if hist_agenda is None:

                hist_agenda = HistAgenda.objects.filter(
                    title_slug=agenda.title_slug
                ).first()


            # ==========================================
            # 3. UPDATE HISTAGENDA
            # ==========================================
            if hist_agenda:

                hist_agenda.observation = agenda.observation

                hist_agenda.start_time_new = agenda.start_time
                hist_agenda.end_time_new = agenda.end_time

                hist_agenda.location_new = agenda.location

                hist_agenda.is_cancel = agenda.is_cancel
                hist_agenda.is_active = agenda.is_active
                hist_agenda.status = agenda.status

                hist_agenda.save()

                print("====================================")
                print("HISTAGENDA UPDATED")
                print("HistAgenda ID:", hist_agenda.pk)
                print(
                    "HistAgenda Observation:",
                    hist_agenda.observation
                )
                print("====================================")

            else:

                print("====================================")
                print(
                    "WARNING: HistAgenda not found "
                    "for Agenda ID:",
                    agenda.pk
                )
                print(
                    "Agenda title_slug:",
                    agenda.title_slug
                )
                print("====================================")


            # ==========================================
            # 4. VERIFY BOTH DATABASE TABLES
            # ==========================================
            check_agenda = Agenda.objects.get(
                pk=agenda.pk
            )

            print("FINAL AGENDA OBSERVATION:")
            print(check_agenda.observation)

            if hist_agenda:

                check_hist = HistAgenda.objects.get(
                    pk=hist_agenda.pk
                )

                print("FINAL HISTAGENDA OBSERVATION:")
                print(check_hist.observation)


            messages.success(
                request,
                "Komentariu rai ho susesu."
            )

            return redirect(
                'concludedAgenda_list'
            )

        else:

            print("====================================")
            print("FORM INVALID")
            print(commentagendaform.errors)
            print("====================================")
    else:
        commentagendaform = CommentAgendaForm(
            instance=single_agenda
        )
    context = {
        'single_agenda': single_agenda,
        'commentagendaform': commentagendaform,
        'v': '/concluded-agenda/comment/add',
    }


    return render(
        request,
        'event/comment_agenda_add.html',
        context
    )


# ============================================= Comment Canceled Agenda Add ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def commentCaAgenda_add(request, pk):

    single_agenda = get_object_or_404(Agenda, pk=pk)

    if request.method == "POST":

        commentagendaform = CommentAgendaForm(
            request.POST,
            request.FILES,
            instance=single_agenda
        )

        if commentagendaform.is_valid():

            # ==========================================
            # UPDATE AGENDA
            # ==========================================
            agenda = commentagendaform.save()

            # ==========================================
            # UPDATE HISTAGENDA
            # ==========================================
            hist_agenda = HistAgenda.objects.filter(
                pk=agenda.pk
            ).first()

            if hist_agenda:

                hist_agenda.start_time_new = agenda.start_time
                hist_agenda.end_time_new = agenda.end_time
                hist_agenda.location_new = agenda.location
                hist_agenda.observation = agenda.observation
                hist_agenda.is_cancel = agenda.is_cancel
                hist_agenda.is_active = agenda.is_active
                hist_agenda.status = agenda.status

                hist_agenda.save()

            messages.success(
                request,
                "Komentariu rai ho susesu."
            )

            return redirect('canceledAgenda_list')

        else:

            # Important for checking why POST failed
            print("FORM INVALID")
            print(commentagendaform.errors)

    else:

        commentagendaform = CommentAgendaForm(
            instance=single_agenda
        )


    # ==========================================
    # CONTEXT
    # Must be OUTSIDE the if/else
    # ==========================================

    context = {
        'single_agenda': single_agenda,
        'commentagendaform': commentagendaform,
        'v': '/canceled-agenda/comment/add',
    }


    return render(
        request,
        'event/comment_agenda_add.html',
        context
    )


# ============================================= Comment running Agenda Add ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def commentRuAgenda_add(request, pk):
    
    # single_informative = request.POST.get('informative_id')
    single_agenda = Agenda.objects.get(id=pk)

    if request.method == "POST":
        commentagendaform = CommentAgendaForm(
            request.POST, request.FILES, instance=single_agenda)
        if commentagendaform.is_valid():
            commentagendaform = commentagendaform.save(commit=False)
            commentagendaform.title = single_agenda.title
            commentagendaform.title_slug = single_agenda.title_slug
            commentagendaform.institution = single_agenda.institution
            commentagendaform.attendence = single_agenda.attendence
            commentagendaform.start_time = single_agenda.start_time
            commentagendaform.end_time = single_agenda.end_time
            commentagendaform.single_agenda = single_agenda
            commentagendaform.save()
            sgl_agenda = Agenda.objects.get(pk=single_agenda.id)
            sgl_hagenda = HistAgenda.objects.get(pk=single_agenda.id)
            sgl_hagenda.start_time_new = sgl_agenda.start_time
            sgl_hagenda.end_time_new = sgl_agenda.end_time
            sgl_hagenda.observation = sgl_agenda.observation
            sgl_hagenda.save()

            messages.success(request, ("New data is added successfully"))
            a = request.path
            head_tail = os.path.split(a)
            v = head_tail[0]
            print(v)

            if v == "/running-agenda/comment/add":
                return redirect('runningAgenda_list')

    else:
        single_agenda = Agenda.objects.get(pk=pk)
        commentagendaform = CommentAgendaForm(instance=single_agenda)
        a = request.path
        head_tail = os.path.split(a)
        v = head_tail[0]

        context = {
            'single_agenda': single_agenda,
            'commentagendaform': commentagendaform,
            'v': v
        }
    return render(request, 'event/comment_agenda_add.html', context)


# ======================================== List Request Agenda ================================================================

@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def requestedagenda_list(request):
    context = {
    }
    return render(request, 'event/request_list.html', context)


# ============================================= Request Agenda Add ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def requestedagenda_add(request):
    if request.method == "POST":
        requestedagendaform = RequestedAgendaForm(request.POST)
        if requestedagendaform.is_valid():
            requestedagendaform = requestedagendaform.save(commit=False)
            requestedagendaform.user = request.user
            requestedagendaform.status = "Pending"
            requestedagendaform.save()

            messages.success(request, ("New data is added successfully"))

        return redirect('requestedagenda_list')

    else:
        requestedagendaform = RequestedAgendaForm()

        context = {
            'requestedagendaform': requestedagendaform,
        }
    return render(request, 'event/request_add.html', context)


# ============================================= Requeste Agenda Edit ================================================================

@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def requestedagenda_edit(request, pk):

    if request.method == "POST":
        single_requestedagenda = RequestAgenda.objects.get(pk=pk)
        requestedagendaform = RequestedAgendaForm(
            request.POST, request.FILES, instance=single_requestedagenda)
        if requestedagendaform.is_valid():
            requestedagendaform.save()
        messages.success(request, ("Date is updated"))
        return redirect('requestedagenda_list')

    else:
        single_requestedagenda = RequestAgenda.objects.get(pk=pk)
        requestedagendaform = RequestedAgendaForm(
            instance=single_requestedagenda)

        context = {
            'single_requestedagenda': single_requestedagenda,
            'requestedagendaform': requestedagendaform,
        }
        return render(request, 'event/request_edit.html', context)

# ======================================== Delete Requesting Agenda ================================================================

@allowed_users(allowed_roles=['sii_admin','ajenda_admin'])
def requestedagenda_delete(request, pk):
    single_requestedagenda = RequestAgenda.objects.get(id=pk)
    single_requestedagenda.delete()
    messages.success(request, ("Delete successfully"))
    return redirect('requestedagenda_list')

# ========================================  Requesting Agenda Read ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def requestedagenda_read(request):
    all_requestedagenda = RequestAgenda.objects.all()
    for a in all_requestedagenda:
        if a.status == 'Pending':
            a.status = "Read"
            a.save()
    return redirect('requestedagenda_list')

# ======================================== Waitting Requesting Agenda ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def waitting_requestedagenda_list(request, pk):

    context = {
    }
    return render(request, 'event/request_waitting_list.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def waitting_requestedagendauga_list(request):
    context = {
    }
    return render(request, 'event/waitting/request_waittinguga_list.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def waitting_requestedagendauap_list(request):
    context = {
    }
    return render(request, 'event/waitting/request_waittinguap_list.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def waitting_requestedagendaucvq_list(request):
    context = {
    }
    return render(request, 'event/waitting/request_waittingucvq_list.html', context)

@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def waitting_requestedagendauedc_list(request):
    context = {
    }
    return render(request, 'event/waitting/request_waittinguedc_list.html', context)



# ======================================== Waitting Requesting Agenda ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def approved_requestedagendauga_list(request):
    context = {
    }
    return render(request, 'event/approve/request_approveuga_list.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def approved_requestedagendauap_list(request):
    context = {
    }
    return render(request, 'event/approve/request_approveuap_list.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def approved_requestedagendaucvq_list(request):
    context = {
    }
    return render(request, 'event/approve/request_approveucvq_list.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def approved_requestedagendauedc_list(request):
    context = {
    }
    return render(request, 'event/approve/request_approveuedc_list.html', context)



# ======================================== Aprove Request Agenda ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def requestedagenda_approve(request, pk):
    all_requestedagenda = RequestAgenda.objects.get(id=pk)
    all_requestedagenda.is_active = "True"

    a = Agenda(title=all_requestedagenda.title, title_slug=all_requestedagenda.title_slug, catagenda=all_requestedagenda.catagenda, institution=all_requestedagenda.institution,  start_time=all_requestedagenda.start_time,
               end_time=all_requestedagenda.end_time, location=all_requestedagenda.location, observation="", is_cancel="False", is_active=all_requestedagenda.is_active, status="Pending", created_at=all_requestedagenda.created_at, updated_at=all_requestedagenda.updated_at)
    a.save()

    ha = HistAgenda(title=all_requestedagenda.title, title_slug=all_requestedagenda.title_slug, catagenda=all_requestedagenda.catagenda, institution=all_requestedagenda.institution,  start_time=all_requestedagenda.start_time,
                    end_time=all_requestedagenda.end_time, location=all_requestedagenda.location, observation="", is_cancel="False", is_active=all_requestedagenda.is_active, status="Pending", created_at=all_requestedagenda.created_at, updated_at=all_requestedagenda.updated_at)
    ha.save()

    all_requestedagenda.save()

    return redirect('requestedagenda_list')


# ======================================== List All Informative ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def informative_list(request):
    context = {
    }
    return render(request, 'event/informative_list.html', context)


# ============================================= Informative Add ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def informative_add(request):
    
    if request.method == "POST":
        informativeform = InformativeForm(request.POST)
        if informativeform.is_valid():
            informativeform = informativeform.save(commit=False)
            informativeform.user = request.user
            informativeform.save()
            messages.success(request, ("New data is added successfully"))
        return redirect('informative_list')
    else:
     
        informativeform = InformativeForm()
        context = {
            'informativeform': informativeform,
        }
    return render(request, 'event/informative_add.html', context)

# ============================================= Agenda Edit ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def informative_edit(request, pk):
    if request.method == "POST":
        single_informative = Informative.objects.get(pk=pk)
        informativeform = InformativeForm(
            request.POST, request.FILES, instance=single_informative)
        if informativeform.is_valid():
            informativeform.save()
        messages.success(request, ("Dadus  hadia ona"))
        return redirect('informative_list')

    else:
        single_informative = Informative.objects.get(pk=pk)
        informativeform = InformativeForm(instance=single_informative)

        context = {
            'single_informative': single_informative,
            'informativeform': informativeform,
        }
        return render(request, 'event/informative_edit.html', context)

# ============================================= Agenda Delete ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin'])
def informative_delete(request, pk):

    single_informative = Informative.objects.get(id=pk)
    single_informative.delete()
    messages.success(request, ("Data is deleted successfully"))
    return redirect('informative_list')


# ================================================= Concluded ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def executedInformative_list(request):
   
    context = {
    }
    return render(request, 'event/executed_informative.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def executedInformative_list_detail(request, title_slug):
   
    single_informative = Informative.objects.get(title_slug=title_slug)
    multiple_comment = CommentInformative.objects.filter(
        informative__title_slug=title_slug)
    multiple_comment_count = multiple_comment.count()

    context = {
        'single_informative': single_informative,
        'multiple_comment': multiple_comment,
        'multiple_comment_count': multiple_comment_count,
    }

    return render(request, 'event/executed_informative_detail.html', context)


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def executeInformative_change(request, pk):
    single_informative = Informative.objects.get(id=pk)
    single_informative.is_done = True
    single_informative.save()
    return redirect('executedInformative_list')


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def unexecutedInformative_list(request):
    context = {
    }
    return render(request, 'event/unexecuted_informative.html', context)

# ================================================= Completed Informative ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def completedInformative_list(request):
    context = {
    }
    return render(request, 'event/completed_informative.html', context)

# ============================================= Comment Executed Informative Add ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def commentExInformative_add(request, pk):
    
    single_informative = Informative.objects.get(id=pk)

    if request.method == "POST":
        commentinformativeform = CommentInformativeForm(request.POST)
        if commentinformativeform.is_valid():
            commentinformativeform = commentinformativeform.save(commit=False)
            commentinformativeform.informative = single_informative
            commentinformativeform.is_active = True
            commentinformativeform.save()

            single_informative.is_comment = True
            single_informative.save()
            messages.success(request, ("New data is added successfully"))
            a = request.path
            head_tail = os.path.split(a)
            v = head_tail[0]

            if v == "/executed-informative/comment/add":
                return redirect('executedInformative_list')

    else:
        commentinformativeform = CommentInformativeForm()
        a = request.path
        head_tail = os.path.split(a)
        v = head_tail[0]

        context = {
            'single_informative': single_informative,
            'commentinformativeform': commentinformativeform,
            'v': v,
        }
    return render(request, 'event/comment_informative_add.html', context)


# ============================================= Comment Executed Informative Add ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def commentExInformative_edit(request, pk):
    single_informative = Informative.objects.get(id=pk)
    single_commentinformative = CommentInformative.objects.filter(
        informative__id=pk).first()

    if request.method == "POST":
        commentinformativeform = CommentInformativeForm(
            request.POST, request.FILES, instance=single_commentinformative)
        if commentinformativeform.is_valid():
            commentinformativeform = commentinformativeform.save(commit=False)
            commentinformativeform.informative = single_informative
            commentinformativeform.is_active = True
            commentinformativeform.save()

            single_informative.is_comment = True
            single_informative.save()

            messages.success(request, ("New data is updated successfully"))
            a = request.path
            head_tail = os.path.split(a)
            v = head_tail[0]

            if v == "/executed-informative/comment/edit":
                return redirect('executedInformative_list')

    else:
        single_commentinformative = CommentInformative.objects.filter(
            informative__id=pk).first()
        commentinformativeform = CommentInformativeForm(
            instance=single_commentinformative)
        a = request.path
        head_tail = os.path.split(a)
        v = head_tail[0]

        context = {
            'single_informative': single_informative,
            'commentinformativeform': commentinformativeform,
            'v': v,
        }
    return render(request, 'event/comment_informative_add.html', context)



@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def agenda_notification_read(request):

    Agenda.objects.filter(
        is_active=True,
        is_cancel=False,
        status='Pending'
    ).update(
        status='Read'
    )

    return redirect('home')

#=============================================  Recipient Management ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def recipient_list(request):
    roles = get_roles(request)
    recipients = (
        AgendaRecipient.objects
        .all()
        .order_by(
            "position",
            "name"
        )
    )

    context = {
        "recipients": recipients,
        "roles":roles
    }

    return render(
        request,
        "event/recipient/list.html",
        context
    )
    
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def recipient_add(request):

    if request.method == "POST":

        form = AgendaRecipientForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Receptor aumenta ho susesu."
            )

            return redirect(
                "recipient_list"
            )

    else:

        form = AgendaRecipientForm()

    context = {
        "form": form,
        "page_title": "Aumenta Receptor Email",
    }

    return render(
        request,
        "event/recipient/form.html",
        context
    )
    
    
# =========================================================
# EDIT RECIPIENT USING UUID
# =========================================================

@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def recipient_edit(request, uuid):

    recipient = get_object_or_404(
        AgendaRecipient,
        uuid=uuid
    )

    if request.method == "POST":

        form = AgendaRecipientForm(
            request.POST,
            instance=recipient
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Receptor atualiza ho susesu."
            )

            return redirect(
                "recipient_list"
            )

    else:

        form = AgendaRecipientForm(
            instance=recipient
        )

    context = {
        "form": form,
        "recipient": recipient,
        "page_title": "Edita Receptor Email",
    }

    return render(
        request,
        "event/recipient/form.html",
        context
    )


# =========================================================
# DELETE RECIPIENT USING UUID
# =========================================================

@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def recipient_delete(request, uuid):

    recipient = get_object_or_404(
        AgendaRecipient,
        uuid=uuid
    )

    if request.method == "POST":

        recipient_name = recipient.name

        recipient.delete()

        messages.success(
            request,
            f'Receptor "{recipient_name}" hamos ho susesu.'
        )

        return redirect(
            "recipient_list"
        )

    context = {
        "recipient": recipient,
    }

    return render(
        request,
        "event/recipient/delete.html",
        context
    )
    
    
# ============================================================
# GET CURRENT NOTIFICATION USER DATA
# ============================================================

def _get_notification_user(request):

    user_id = (
        getattr(
            request,
            "portal_user_id",
            None
        )
        or
        request.session.get(
            "agenda_user_id"
        )
    )

    username = (
        getattr(
            request,
            "portal_user",
            None
        )
        or
        request.session.get(
            "agenda_user"
        )
        or
        ""
    )

    roles = (
        getattr(
            request,
            "portal_roles",
            None
        )
        or
        request.session.get(
            "agenda_roles",
            []
        )
        or
        []
    )

    return (
        user_id,
        username,
        roles,
    )


# ============================================================
# LIVE AJAX NOTIFICATIONS
# ============================================================

def notification_live(request):

    (
        user_id,
        username,
        roles
    ) = _get_notification_user(
        request
    )


    if (
        not user_id
        or
        not roles
    ):

        return JsonResponse({

            "authenticated":
                False,

            "unread_count":
                0,

            "notifications":
                [],
        })


    user_id = str(
        user_id
    )


    notifications_queryset = (
        get_notifications_for_roles(
            roles
        )
    )


    read_ids = set(

        NotificationRead.objects
        .filter(
            central_user_id=user_id
        )
        .values_list(
            "notification_id",
            flat=True
        )
    )


    unread_count = (
        notifications_queryset
        .exclude(
            id__in=read_ids
        )
        .count()
    )


    notification_data = []


    for obj in notifications_queryset[:10]:

        notification_data.append({

            "uuid":
                str(obj.uuid),

            "title":
                obj.title,

            "message":
                obj.message,

            "type":
                obj.notification_type,

            "created_at":
                obj.created_at.strftime(
                    "%d/%m/%Y %H:%M"
                ),

            "is_read":
                obj.id in read_ids,

            "open_url":
                reverse(
                    "notification_open",
                    kwargs={
                        "uuid":
                            obj.uuid
                    }
                ),
        })


    return JsonResponse({

        "authenticated":
            True,

        "unread_count":
            unread_count,

        "notifications":
            notification_data,
    })


# ============================================================
# OPEN + MARK READ
# ============================================================

def notification_open(
    request,
    uuid
):

    (
        user_id,
        username,
        roles
    ) = _get_notification_user(
        request
    )


    if (
        not user_id
        or
        not roles
    ):

        return redirect(
            "home"
        )


    allowed_notifications = (
        get_notifications_for_roles(
            roles
        )
    )


    notification = get_object_or_404(
        allowed_notifications,
        uuid=uuid
    )


    NotificationRead.objects.get_or_create(

        notification=
            notification,

        central_user_id=
            str(user_id),

        defaults={

            "central_username":
                username,

            "read_at":
                timezone.now(),
        }
    )


    if notification.url:

        return redirect(
            notification.url
        )


    return redirect(
        "home"
    )


# ============================================================
# MARK ALL READ
# ============================================================

def notification_mark_all_read(
    request
):

    (
        user_id,
        username,
        roles
    ) = _get_notification_user(
        request
    )


    if (
        not user_id
        or
        not roles
    ):

        return redirect(
            "home"
        )


    user_id = str(
        user_id
    )


    notifications = (
        get_notifications_for_roles(
            roles
        )
    )


    existing_read_ids = set(

        NotificationRead.objects
        .filter(
            central_user_id=user_id
        )
        .values_list(
            "notification_id",
            flat=True
        )
    )


    new_reads = []


    for notification in notifications:

        if (
            notification.id
            not in existing_read_ids
        ):

            new_reads.append(

                NotificationRead(

                    notification=
                        notification,

                    central_user_id=
                        user_id,

                    central_username=
                        username,

                    read_at=
                        timezone.now(),
                )
            )


    if new_reads:

        NotificationRead.objects.bulk_create(
            new_reads,
            ignore_conflicts=True
        )


    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "/"
        )
    )


# ============================================================
# FULL NOTIFICATION LIST
# ============================================================

def notification_list(
    request
):

    (
        user_id,
        username,
        roles
    ) = _get_notification_user(
        request
    )


    if not user_id:

        return redirect(
            "home"
        )


    user_id = str(
        user_id
    )


    notifications = list(

        get_notifications_for_roles(
            roles
        )
    )


    read_ids = set(

        NotificationRead.objects
        .filter(
            central_user_id=user_id
        )
        .values_list(
            "notification_id",
            flat=True
        )
    )


    for obj in notifications:

        obj.user_has_read = (
            obj.id
            in
            read_ids
        )


    context = {

        "notification_list":
            notifications,
    }


    return render(
        request,
        "event/notification_list.html",
        context
    )