from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CatAgenda, Agenda,AgendaRecipient, RequestAgenda, HistAgenda, Informative, CommentInformative
from .form import CategoryAgendaForm, AgendaForm, AgendaRecipientForm,  PostponedAgendaForm, CommentAgendaForm, RequestedAgendaForm, InformativeForm, CommentInformativeForm
from django.contrib.auth.models import User
from agendaapps.authentication.models import User
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.db import transaction
import os
from agendaapps.authentication.decorators import allowed_users
from agenda.utils import get_roles
from django.db.models import Q
from django.utils import timezone
current_datetime = timezone.now()


# Create your views here.
# ======================================== Category Agenda Add ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def categoryagenda_list(request):
    roles = get_roles(request)
    catagendalist = CatAgenda.objects.all()
    if request.method == "POST":
        categoryagendaform = CategoryAgendaForm(request.POST)
        if categoryagendaform.is_valid():
            categoryagendaform.save()

            messages.success(request, ("New data is added"))
        return redirect('categoryagenda_list')

    else:
        categoryagendaform = CategoryAgendaForm()
        context = {
            'categoryagendaform': categoryagendaform,
            'catagendalist': catagendalist,
            'roles':roles
        }
    return render(request, 'event/category_agenda_list.html', context)

# ============================================= Category Agenda Edit ================================================================

@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def categoryagenda_edit(request, pk):
    catagendalist = CatAgenda.objects.all()

    if request.method == "POST":
        single_categoryagenda = CatAgenda.objects.get(pk=pk)
        categoryagendaform = CategoryAgendaForm(
            request.POST, request.FILES, instance=single_categoryagenda)
        if categoryagendaform.is_valid():
            categoryagendaform.save()
        messages.success(request, ("Data is updated"))
        return redirect('categoryagenda_list')
    else:
     
        single_categoryagenda = CatAgenda.objects.get(pk=pk)
        categoryagendaform = CategoryAgendaForm(instance=single_categoryagenda)

        context = {
            'single_categoryagenda': single_categoryagenda,
            'catagendalist': catagendalist,
            'categoryagendaform': categoryagendaform,
        }
        return render(request, 'event/category_agenda_edit.html', context)

# ============================================= Category Agenda Delete ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin'])
def categoryagenda_delete(request, pk):
    single_categoryagenda = CatAgenda.objects.get(id=pk)
    single_categoryagenda.delete()
    messages.success(request, ("Delete successfully"))
    return redirect('categoryagenda_list')

# ======================================== List All Agenda ================================================================
@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def agenda_list(request):
    roles = get_roles(request)
    context = {
        'roles':roles
    }
    return render(request, 'event/agenda_list.html', context)

# ============================================= Agenda Add ================================================================

@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def agenda_add(request):

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
            # Set Agenda status
            # ==========================================

            if agenda.start_time >= current_datetime:

                agenda.status = "Pending"

            elif (
                agenda.start_time <= current_datetime
                and
                agenda.end_time >= current_datetime
            ):

                agenda.status = "Read"

            elif agenda.end_time < current_datetime:

                agenda.status = "Read"

            # ==========================================
            # Save Agenda first
            # ==========================================

            agenda.save()

            # ==========================================
            # IMPORTANT:
            # Save selected Director / Minister
            # from ManyToMany "recipients"
            # ==========================================

            form.save_m2m()

            # ==========================================
            # Create Agenda History
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

                start_time=agenda.start_time,

                start_time_new=agenda.start_time,

                end_time=agenda.end_time,

                end_time_new=agenda.end_time,

                location=agenda.location,

                location_new=agenda.location,

                meeting_type=(
                    agenda.meeting_type.name_type
                ),

                observation=agenda.observation,

                is_cancel=agenda.is_cancel,

                is_active=agenda.is_active,

                status=agenda.status,

                created_at=agenda.created_at,

                updated_at=agenda.updated_at,
            )

            ha.save()

            messages.success(
                request,
                "New Data Added"
            )

            return redirect(
                'agenda_list'
            )

        else:

            # Useful during development
            print("Error: AgendaForm is invalid")
            

    else:

        form = AgendaForm()

    context = {
        'agendaform': form,
    }

    return render(
        request,
        'event/agenda_add.html',
        context
    )
# ============================================= Agenda Edit ================================================================


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def agenda_edit(request, uuid):

    single_agenda = get_object_or_404(
        Agenda,
        uuid=uuid
    )

    if request.method == "POST":

        agendaform = AgendaForm(
            request.POST,
            request.FILES,
            instance=single_agenda
        )

        if agendaform.is_valid():

            agendaform.save()

            messages.success(
                request,
                "Ajenda atualiza ho susesu."
            )

            return redirect(
                "agenda_list"
            )

    else:

        agendaform = AgendaForm(
            instance=single_agenda
        )

    context = {
        "single_agenda": single_agenda,
        "agendaform": agendaform,
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


@allowed_users(allowed_roles=['sii_admin','ajenda_admin','ajenda_user'])
def upcomingAgenda_list_detail(request, title_slug):
    single_agenda = Agenda.objects.get(title_slug=title_slug)
    all_agenda = Agenda.objects.all()

    context = {
        'single_agenda': single_agenda, 'all_agenda': all_agenda,
    }
    return render(request, 'event/upcoming_agenda_detail.html', context)


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