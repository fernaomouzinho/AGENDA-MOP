from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CatAgenda, Agenda, RequestAgenda, HistAgenda, Informative, CommentInformative
from .form import CategoryAgendaForm, AgendaForm, PostponedAgendaForm, CommentAgendaForm, RequestedAgendaForm, InformativeForm, CommentInformativeForm
from django.contrib.auth.models import User
from eventapps.authentication.models import User
from datetime import datetime
import os
from django.db.models import Q
current_datetime = datetime.now()


# Create your views here.
# ======================================== Category Agenda Add ================================================================
@login_required(login_url="/login/")
def categoryagenda_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    catagendalist = CatAgenda.objects.all()

    if request.method == "POST":
        categoryagendaform = CategoryAgendaForm(request.POST)
        if categoryagendaform.is_valid():
            categoryagendaform.save()

            messages.success(request, ("New data is added"))
        return redirect('categoryagenda_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        categoryagendaform = CategoryAgendaForm()
        context = {
            'userprofile': userprofile,
            'categoryagendaform': categoryagendaform,
            'catagendalist': catagendalist,
        }
    return render(request, 'event/category_agenda_list.html', context)


# ============================================= Category Agenda Edit ================================================================


@login_required(login_url='login')
def categoryagenda_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

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
        userprofile = User.objects.get(id=request.user.id)
        single_categoryagenda = CatAgenda.objects.get(pk=pk)
        categoryagendaform = CategoryAgendaForm(instance=single_categoryagenda)

        context = {
            'userprofile': userprofile,
            'single_categoryagenda': single_categoryagenda,
            'catagendalist': catagendalist,
            'categoryagendaform': categoryagendaform,
        }
        return render(request, 'event/category_agenda_edit.html', context)

# ============================================= Category Agenda Delete ================================================================


@login_required(login_url='login')
def categoryagenda_delete(request, pk):
    single_categoryagenda = CatAgenda.objects.get(id=pk)
    single_categoryagenda.delete()
    messages.success(request, ("Delete successfully"))
    return redirect('categoryagenda_list')


# ======================================== List All Agenda ================================================================
@login_required(login_url="/login/")
def agenda_list(request):

    context = {
    }
    return render(request, 'event/agenda_list.html', context)

# ============================================= Agenda Add ================================================================


@login_required(login_url='login')
def agenda_add(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        agendaform = AgendaForm(request.POST, request.FILES)
        if agendaform.is_valid():
            agendaform = agendaform.save(commit=False)
            agendaform.user = request.user
            if agendaform.start_time >= current_datetime:
                agendaform.status = "Pending"

            elif agendaform.start_time <= current_datetime and agendaform.end_time >= current_datetime:
                agendaform.status = "Read"

            elif agendaform.end_time < current_datetime:
                agendaform.status = "Read"
            last_hist = HistAgenda.objects.all().first()

            ha = HistAgenda(id=agendaform.id, user=request.user, title=agendaform.title, title_slug=agendaform.title_slug, institution=agendaform.institution, start_time=agendaform.start_time, start_time_new=agendaform.start_time, end_time=agendaform.end_time, end_time_new=agendaform.end_time,
                            location=agendaform.location, location_new=agendaform.location, observation=agendaform.observation, is_cancel=agendaform.is_cancel, is_active=agendaform.is_active, status=agendaform.status, created_at=agendaform.created_at, updated_at=agendaform.updated_at)
            ha.save()

            agendaform.save()

            messages.success(request, ("New Data Added"))
        return redirect('agenda_list')
    else:
        userprofile = User.objects.get(id=request.user.id)
        agendaform = AgendaForm()
        context = {
            'userprofile': userprofile,
            'agendaform': agendaform,
        }

    return render(request, 'event/agenda_add.html', context)

# ============================================= Agenda Edit ================================================================


@login_required(login_url='login')
def agenda_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        single_agenda = Agenda.objects.get(pk=pk)
        agendaform = AgendaForm(
            request.POST, request.FILES, instance=single_agenda)
        if agendaform.is_valid():
            agendaform.save()
        messages.success(request, ("Data is updated"))
        return redirect('agenda_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_agenda = Agenda.objects.get(pk=pk)
        agendaform = AgendaForm(instance=single_agenda)

        context = {
            'userprofile': userprofile,
            'single_agenda': single_agenda,
            'agendaform': agendaform,
        }
        return render(request, 'event/agenda_edit.html', context)

# ============================================= Agenda Delete ================================================================


@login_required(login_url='login')
def agenda_delete(request, pk):
    single_agenda = Agenda.objects.get(id=pk)
    single_agenda.delete()
    messages.success(request, ("Delete successfully"))
    return redirect('agenda_list')


# ================================================= Completed Agenda ================================================================
@login_required(login_url="/login/")
def completedAgenda_list(request):
    context = {
    }
    return render(request, 'event/completed_agenda.html', context)


# ================================================= Concluded Agenda ================================================================
@login_required(login_url="/login/")
def concludedAgenda_list(request):
    context = {
    }
    return render(request, 'event/concluded_agenda.html', context)


@login_required(login_url="/login/")
def concludedAgenda_list_detail(request, title_slug):
    single_agenda = Agenda.objects.get(title_slug=title_slug)
    all_agenda = Agenda.objects.all()

    context = {
        'single_agenda': single_agenda, 'all_agenda': all_agenda,
    }
    return render(request, 'event/concluded_agenda_detail.html', context)

# ======================================== Canceled ================================================================


@login_required(login_url="/login/")
def canceledAgenda_list(request):
    context = {
    }
    return render(request, 'event/canceled_agenda.html', context)


@login_required(login_url="/login/")
def canceledAgenda_list_detail(request, title_slug):
    single_agenda = Agenda.objects.get(title_slug=title_slug)
    all_agenda = Agenda.objects.all()

    context = {
        'single_agenda': single_agenda, 'all_agenda': all_agenda,
    }
    return render(request, 'event/canceled_agenda_detail.html', context)

# ========================================= Running ================================================================


@login_required(login_url="/login/")
def runningAgenda_list(request):
    current_datetime = datetime.now()
    context = {
    }
    return render(request, 'event/running_agenda.html', context)


@login_required(login_url="/login/")
def runningAgenda_list_detail(request, title_slug):
    context = {
    }
    return render(request, 'event/running_agenda_detail.html', context)

# ======================================== Upcoming ================================================================


@login_required(login_url="/login/")
def upcomingAgenda_list(request):
    context = {
    }
    return render(request, 'event/upcoming_agenda.html', context)


@login_required(login_url="/login/")
def upcomingAgenda_list_detail(request, title_slug):
    single_agenda = Agenda.objects.get(title_slug=title_slug)
    all_agenda = Agenda.objects.all()

    context = {
        'single_agenda': single_agenda, 'all_agenda': all_agenda,
    }
    return render(request, 'event/upcoming_agenda_detail.html', context)


@login_required(login_url="/login/")
def upcomingAgenda_edit(request, pk):
    single_agenda = Agenda.objects.get(id=pk)
    context = {
        'single_agenda': single_agenda,
    }
    return render(request, 'event/upcoming_agenda_edit.html', context)


@login_required(login_url='login')
def upcomingAgenda_delete(request, pk):

    single_agenda = Agenda.objects.get(id=pk)
    single_agenda.delete()
    messages.success(request, ("Dadus hamos ona"))
    return redirect('upcoming_view')


@login_required(login_url='login')
def upcomingAgenda_cancel(request, pk):
    single_agenda = Agenda.objects.get(id=pk)
    single_agenda.is_cancel = "True"
    single_agenda.save()
    return redirect('canceledAgenda_list')


@login_required(login_url='login')
def upcomingAgenda_read(request):
    all_agenda = Agenda.objects.all()
    for a in all_agenda:
        if a.status == 'Pending':
            a.status = "Read"
            a.save()
    return redirect('upcomingAgenda_list')


# ======================================== Postpone ================================================================
@login_required(login_url="/login/")
def postponeAgenda_list(request, pk):

    if not request.user.is_authenticated:
        return redirect('login')

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
        userprofile = User.objects.get(id=request.user.id)
        single_agenda = Agenda.objects.get(pk=pk)
        postponedagendaform = PostponedAgendaForm(instance=single_agenda)

        context = {
            'userprofile': userprofile,
            'single_agenda': single_agenda,
            'postponedagendaform': postponedagendaform,
        }

    return render(request, 'event/postponed_agenda.html', context)


# ============================================= Comment Conclude Agenda Add ================================================================
@login_required(login_url='login')
def commentCoAgenda_add(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    # single_informative = request.POST.get('informative_id')
    single_agenda = Agenda.objects.get(id=pk)

    if request.method == "POST":
        commentagendaform = CommentAgendaForm(
            request.POST, request.FILES, instance=single_agenda)
        if commentagendaform.is_valid():
            commentagendaform = commentagendaform.save(commit=False)
            commentagendaform.user = request.user
            commentagendaform.title = single_agenda.title
            commentagendaform.title_slug = single_agenda.title_slug
            commentagendaform.institution = single_agenda.institution
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

            if v == "/concluded-agenda/comment/add":
                return redirect('concludedAgenda_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_agenda = Agenda.objects.get(pk=pk)
        commentagendaform = CommentAgendaForm(instance=single_agenda)
        a = request.path
        head_tail = os.path.split(a)
        v = head_tail[0]

        context = {
            'userprofile': userprofile,
            'single_agenda': single_agenda,
            'commentagendaform': commentagendaform,
            'v': v,
        }
    return render(request, 'event/comment_agenda_add.html', context)


# ============================================= Comment Canceled Agenda Add ================================================================
@login_required(login_url='login')
def commentCaAgenda_add(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    # single_informative = request.POST.get('informative_id')
    single_agenda = Agenda.objects.get(id=pk)

    if request.method == "POST":
        commentagendaform = CommentAgendaForm(
            request.POST, request.FILES, instance=single_agenda)
        if commentagendaform.is_valid():
            commentagendaform = commentagendaform.save(commit=False)
            commentagendaform.user = request.user
            commentagendaform.title = single_agenda.title
            commentagendaform.title_slug = single_agenda.title_slug
            commentagendaform.institution = single_agenda.institution
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

            if v == "/canceled-agenda/comment/add":
                return redirect('canceledAgenda_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_agenda = Agenda.objects.get(pk=pk)
        commentagendaform = CommentAgendaForm(instance=single_agenda)
        a = request.path
        head_tail = os.path.split(a)
        v = head_tail[0]

        context = {
            'userprofile': userprofile,
            'single_agenda': single_agenda,
            'commentagendaform': commentagendaform,
            'v': v
        }
    return render(request, 'event/comment_agenda_add.html', context)


# ============================================= Comment running Agenda Add ================================================================
@login_required(login_url='login')
def commentRuAgenda_add(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    # single_informative = request.POST.get('informative_id')
    single_agenda = Agenda.objects.get(id=pk)

    if request.method == "POST":
        commentagendaform = CommentAgendaForm(
            request.POST, request.FILES, instance=single_agenda)
        if commentagendaform.is_valid():
            commentagendaform = commentagendaform.save(commit=False)
            commentagendaform.user = request.user
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
        userprofile = User.objects.get(id=request.user.id)
        single_agenda = Agenda.objects.get(pk=pk)
        commentagendaform = CommentAgendaForm(instance=single_agenda)
        a = request.path
        head_tail = os.path.split(a)
        v = head_tail[0]

        context = {
            'userprofile': userprofile,
            'single_agenda': single_agenda,
            'commentagendaform': commentagendaform,
            'v': v
        }
    return render(request, 'event/comment_agenda_add.html', context)


# ======================================== List Request Agenda ================================================================

@login_required(login_url="/login/")
def requestedagenda_list(request):

    context = {
    }
    return render(request, 'event/request_list.html', context)


# ============================================= Request Agenda Add ================================================================
@login_required(login_url='login')
def requestedagenda_add(request):
    if not request.user.is_authenticated:
        return redirect('login')

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
        userprofile = User.objects.get(id=request.user.id)
        requestedagendaform = RequestedAgendaForm()

        context = {
            'userprofile': userprofile,
            'requestedagendaform': requestedagendaform,
        }
    return render(request, 'event/request_add.html', context)


# ============================================= Requeste Agenda Edit ================================================================

@login_required(login_url='login')
def requestedagenda_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        single_requestedagenda = RequestAgenda.objects.get(pk=pk)
        requestedagendaform = RequestedAgendaForm(
            request.POST, request.FILES, instance=single_requestedagenda)
        if requestedagendaform.is_valid():
            requestedagendaform.save()
        messages.success(request, ("Date is updated"))
        return redirect('requestedagenda_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_requestedagenda = RequestAgenda.objects.get(pk=pk)
        requestedagendaform = RequestedAgendaForm(
            instance=single_requestedagenda)

        context = {
            'userprofile': userprofile,
            'single_requestedagenda': single_requestedagenda,
            'requestedagendaform': requestedagendaform,
        }
        return render(request, 'event/request_edit.html', context)

# ======================================== Delete Requesting Agenda ================================================================


@login_required(login_url='login')
def requestedagenda_delete(request, pk):
    single_requestedagenda = RequestAgenda.objects.get(id=pk)
    single_requestedagenda.delete()
    messages.success(request, ("Delete successfully"))
    return redirect('requestedagenda_list')

# ========================================  Requesting Agenda Read ================================================================


@login_required(login_url='login')
def requestedagenda_read(request):
    all_requestedagenda = RequestAgenda.objects.all()
    for a in all_requestedagenda:
        if a.status == 'Pending':
            a.status = "Read"
            a.save()
    return redirect('requestedagenda_list')

# ======================================== Waitting Requesting Agenda ================================================================


@login_required(login_url="/login/")
def waitting_requestedagenda_list(request, pk):

    context = {
    }
    return render(request, 'event/request_waitting_list.html', context)


@login_required(login_url="/login/")
def waitting_requestedagendauga_list(request):
    context = {
    }
    return render(request, 'event/waitting/request_waittinguga_list.html', context)


@login_required(login_url="/login/")
def waitting_requestedagendauap_list(request):
    context = {
    }
    return render(request, 'event/waitting/request_waittinguap_list.html', context)


@login_required(login_url="/login/")
def waitting_requestedagendaucvq_list(request):
    context = {
    }
    return render(request, 'event/waitting/request_waittingucvq_list.html', context)


@login_required(login_url="/login/")
def waitting_requestedagendauedc_list(request):
    context = {
    }
    return render(request, 'event/waitting/request_waittinguedc_list.html', context)


# ======================================== Aprove Request Agenda ================================================================


@login_required(login_url='login')
def requestedagenda_approve(request, pk):
    all_requestedagenda = RequestAgenda.objects.get(id=pk)
    all_requestedagenda.is_active = "True"

    a = Agenda(user=all_requestedagenda.user, title=all_requestedagenda.title, title_slug=all_requestedagenda.title_slug, catagenda=all_requestedagenda.catagenda, institution=all_requestedagenda.institution,  start_time=all_requestedagenda.start_time,
               end_time=all_requestedagenda.end_time, location=all_requestedagenda.location, observation="", is_cancel="False", is_active=all_requestedagenda.is_active, status="Pending", created_at=all_requestedagenda.created_at, updated_at=all_requestedagenda.updated_at)
    a.save()

    ha = HistAgenda(user=all_requestedagenda.user, title=all_requestedagenda.title, title_slug=all_requestedagenda.title_slug, catagenda=all_requestedagenda.catagenda, institution=all_requestedagenda.institution,  start_time=all_requestedagenda.start_time,
                    end_time=all_requestedagenda.end_time, location=all_requestedagenda.location, observation="", is_cancel="False", is_active=all_requestedagenda.is_active, status="Pending", created_at=all_requestedagenda.created_at, updated_at=all_requestedagenda.updated_at)
    ha.save()

    all_requestedagenda.save()

    return redirect('requestedagenda_list')


# ======================================== List All Informative ================================================================


@login_required(login_url="/login/")
def informative_list(request):
    context = {
    }
    return render(request, 'event/informative_list.html', context)


# ============================================= Informative Add ================================================================
@login_required(login_url='login')
def informative_add(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        informativeform = InformativeForm(request.POST)
        if informativeform.is_valid():
            informativeform = informativeform.save(commit=False)
            informativeform.user = request.user
            informativeform.save()
            messages.success(request, ("New data is added successfully"))
        return redirect('informative_list')
    else:
        userprofile = User.objects.get(id=request.user.id)
        informativeform = InformativeForm()
        context = {
            'userprofile': userprofile,
            'informativeform': informativeform,
        }
    return render(request, 'event/informative_add.html', context)

# ============================================= Agenda Edit ================================================================


@login_required(login_url='login')
def informative_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        single_informative = Informative.objects.get(pk=pk)
        informativeform = InformativeForm(
            request.POST, request.FILES, instance=single_informative)
        if informativeform.is_valid():
            informativeform.save()
        messages.success(request, ("Dadus  hadia ona"))
        return redirect('informative_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_informative = Informative.objects.get(pk=pk)
        informativeform = InformativeForm(instance=single_informative)

        context = {
            'userprofile': userprofile,
            'single_informative': single_informative,
            'informativeform': informativeform,
        }
        return render(request, 'event/informative_edit.html', context)

# ============================================= Agenda Delete ================================================================


@login_required(login_url='login')
def informative_delete(request, pk):

    single_informative = Informative.objects.get(id=pk)
    single_informative.delete()
    messages.success(request, ("Data is deleted successfully"))
    return redirect('informative_list')


# ================================================= Concluded ================================================================
@login_required(login_url="/login/")
def executedInformative_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {
    }
    return render(request, 'event/executed_informative.html', context)


@login_required(login_url="/login/")
def executedInformative_list_detail(request, title_slug):
    if not request.user.is_authenticated:
        return redirect('login')

    single_informative = Informative.objects.get(title_slug=title_slug)
    multiple_comment = CommentInformative.objects.filter(
        informative__title_slug=title_slug)
    multiple_comment_count = multiple_comment.count()
    userprofile = User.objects.get(id=request.user.id)

    context = {
        'userprofile': userprofile,
        'single_informative': single_informative,
        'multiple_comment': multiple_comment,
        'multiple_comment_count': multiple_comment_count,
    }

    return render(request, 'event/executed_informative_detail.html', context)


@login_required(login_url='login')
def executeInformative_change(request, pk):
    single_informative = Informative.objects.get(id=pk)
    single_informative.is_done = True
    single_informative.save()
    return redirect('executedInformative_list')


@login_required(login_url="/login/")
def unexecutedInformative_list(request):
    context = {
    }
    return render(request, 'event/unexecuted_informative.html', context)

# ================================================= Completed Informative ================================================================


@login_required(login_url="/login/")
def completedInformative_list(request):
    context = {
    }
    return render(request, 'event/completed_informative.html', context)

# ============================================= Comment Executed Informative Add ================================================================


@login_required(login_url='login')
def commentExInformative_add(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    single_informative = Informative.objects.get(id=pk)

    if request.method == "POST":
        commentinformativeform = CommentInformativeForm(request.POST)
        if commentinformativeform.is_valid():
            commentinformativeform = commentinformativeform.save(commit=False)
            commentinformativeform.user = request.user
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
        userprofile = User.objects.get(id=request.user.id)
        commentinformativeform = CommentInformativeForm()
        a = request.path
        head_tail = os.path.split(a)
        v = head_tail[0]

        context = {
            'userprofile': userprofile,
            'single_informative': single_informative,
            'commentinformativeform': commentinformativeform,
            'v': v,
        }
    return render(request, 'event/comment_informative_add.html', context)


# ============================================= Comment Executed Informative Add ================================================================
@login_required(login_url='login')
def commentExInformative_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    single_informative = Informative.objects.get(id=pk)
    single_commentinformative = CommentInformative.objects.filter(
        informative__id=pk).first()

    if request.method == "POST":
        commentinformativeform = CommentInformativeForm(
            request.POST, request.FILES, instance=single_commentinformative)
        if commentinformativeform.is_valid():
            commentinformativeform = commentinformativeform.save(commit=False)
            commentinformativeform.user = request.user
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
        userprofile = User.objects.get(id=request.user.id)
        single_commentinformative = CommentInformative.objects.filter(
            informative__id=pk).first()
        commentinformativeform = CommentInformativeForm(
            instance=single_commentinformative)
        a = request.path
        head_tail = os.path.split(a)
        v = head_tail[0]

        context = {
            'userprofile': userprofile,
            'single_informative': single_informative,
            'commentinformativeform': commentinformativeform,
            'v': v,
        }
    return render(request, 'event/comment_informative_add.html', context)
