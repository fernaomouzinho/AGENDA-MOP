from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Agenda, HistAgenda ,Informative, CommentInformative
from .form import AgendaForm, PostponedAgendaForm, CommentAgendaForm, InformativeForm, CommentInformativeForm
from django.contrib.auth.models import User
from datetime import datetime


# Create your views here.

#======================================== List All Agenda ================================================================
@login_required(login_url="/login/")
def agenda_list(request):
    
    context = {
    }
    return render(request, 'event/agenda_list.html', context)

#============================================= Agenda Add ================================================================
@login_required(login_url='login')
def agenda_add(request):
    if not request.user.is_authenticated :
        return redirect('login')

    if request.method == "POST":
        agendaform = AgendaForm(request.POST, request.FILES)
        if agendaform.is_valid():
            agendaform = agendaform.save(commit=False)
            agendaform.user=request.user
            agendaform.status="Pending"
            ha = HistAgenda(user=request.user, title=agendaform.title, title_slug=agendaform.title_slug, institution=agendaform.institution,attendence=agendaform.attendence,start_time=agendaform.start_time,start_time_new=agendaform.start_time,end_time=agendaform.end_time,end_time_new=agendaform.end_time,location=agendaform.location,location_new=agendaform.location,observation=agendaform.observation,is_cancel=agendaform.is_cancel,is_active=agendaform.is_active,status=agendaform.status,created_at=agendaform.created_at,updated_at=agendaform.updated_at)
            ha.save()

            agendaform.save()

            messages.success(request, ("New Data Added"))
        return redirect('agenda_list')
    else:
        userprofile = User.objects.get(id=request.user.id)
        agendaform = AgendaForm()
        context = {
            'userprofile':userprofile,
            'agendaform': agendaform,
        }

    return render(request, 'event/agenda_add.html', context)

#============================================= Agenda Edit ================================================================
@login_required(login_url='login')
def agenda_edit(request,pk):
    if not request.user.is_authenticated :
        return redirect('login')

    if request.method == "POST":
        single_agenda = Agenda.objects.get(pk=pk)
        agendaform = AgendaForm(request.POST, request.FILES, instance=single_agenda)
        if agendaform.is_valid():
            agendaform.save()
        messages.success(request, ("Dadus  hadia ona"))
        return redirect('agenda_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_agenda= Agenda.objects.get(pk=pk)
        agendaform = AgendaForm(instance=single_agenda)

        context = {
        'userprofile':userprofile,
        'single_agenda': single_agenda,
        'agendaform': agendaform,
        }
        return render(request, 'event/agenda_edit.html', context)

#============================================= Agenda Delete ================================================================
@login_required(login_url='login')
def agenda_delete(request,pk):
    single_agenda = Agenda.objects.get(id=pk)
    single_agenda.delete()
    messages.success(request, ("Delete successfully"))
    return redirect('agenda_list')


#================================================= Completed Agenda ================================================================
@login_required(login_url="/login/")
def completedAgenda_list(request):
    context = {
    }
    return render(request, 'event/completed_agenda.html', context)



#================================================= Concluded Agenda ================================================================
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
        'single_agenda':single_agenda,'all_agenda':all_agenda,
    }
    return render(request, 'event/concluded_agenda_detail.html', context)

#======================================== Canceled ================================================================

@login_required(login_url="/login/")
def canceledAgenda_list(request):
    context = {
    }
    return render(request, 'event/canceled_agenda.html', context)

@login_required(login_url="/login/")
def canceledAgenda_list_detail(request):
    context = {
    }
    return render(request, 'event/canceled_agenda_detail.html', context)

#========================================= Running ================================================================
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

#======================================== Upcoming ================================================================
@login_required(login_url="/login/")
def upcomingAgenda_list(request):
    context = {
    }
    return render(request, 'event/upcoming_agenda.html', context)


@login_required(login_url="/login/")
def upcomingAgenda_list_detail(request, title_slug):
    context = {
    }
    return render(request, 'event/upcoming_agenda_detail.html', context)


@login_required(login_url="/login/")
def upcomingAgenda_edit(request, pk):
    single_agenda = Agenda.objects.get(id=pk)
    context = {
        'single_agenda':single_agenda,
    }
    return render(request, 'event/upcoming_agenda_edit.html', context)

@login_required(login_url='login')
def upcomingAgenda_delete(request,pk):

    single_agenda = Agenda.objects.get(id=pk)
    single_agenda.delete()
    messages.success(request, ("Dadus hamos ona"))
    return redirect('upcoming_view')

@login_required(login_url='login')
def upcomingAgenda_cancel(request,pk):
    single_agenda = Agenda.objects.get(id=pk)
    single_agenda.is_cancel = "True"
    single_agenda.save()
    return redirect('canceledAgenda_list')

@login_required(login_url='login')
def upcomingAgenda_read(request):
    all_agenda = Agenda.objects.all()
    for a in all_agenda:
        if a.status=='Pending':
            a.status="Read"
            a.save()
    return redirect('upcomingAgenda_list')


#======================================== Postpone ================================================================
@login_required(login_url="/login/")
def postponeAgenda_list(request, pk):

    if not request.user.is_authenticated :
        return redirect('login')

    if request.method == "POST":
        single_agenda = Agenda.objects.get(pk=pk)
        postponedagendaform = PostponedAgendaForm(request.POST, request.FILES, instance=single_agenda)
        if postponedagendaform.is_valid():
            postponedagendaform.save()
            sgl_agenda = Agenda.objects.get(pk=single_agenda.id)
            sgl_hagenda = HistAgenda.objects.get(pk=single_agenda.id)
            sgl_hagenda.start_time_new = sgl_agenda.start_time
            sgl_hagenda.end_time_new   = sgl_agenda.end_time
            sgl_hagenda.save()

        messages.success(request, ("Data changed succesfully"))
        return redirect('agenda_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_agenda= Agenda.objects.get(pk=pk)
        postponedagendaform = PostponedAgendaForm(instance=single_agenda)

        context = {
        'userprofile':userprofile,
        'single_agenda': single_agenda,
        'postponedagendaform': postponedagendaform,
        }

    return render(request, 'event/postponed_agenda.html', context)


#============================================= Comment Agenda Add ================================================================
@login_required(login_url='login')
def commentAgenda_add(request, pk):
    if not request.user.is_authenticated :
        return redirect('login')

    #single_informative = request.POST.get('informative_id')
    single_agenda = Agenda.objects.get(id=pk)

    if request.method == "POST":
        commentagendaform = CommentAgendaForm(request.POST, request.FILES, instance=single_agenda)
        if commentagendaform.is_valid():
            commentagendaform = commentagendaform.save(commit=False)
            commentagendaform.user=request.user
            commentagendaform.title=single_agenda.title
            commentagendaform.title_slug=single_agenda.title_slug
            commentagendaform.institution=single_agenda.institution
            commentagendaform.attendence=single_agenda.attendence
            commentagendaform.start_time=single_agenda.start_time
            commentagendaform.end_time=single_agenda.end_time
            commentagendaform.single_agenda=single_agenda
            commentagendaform.save()
            sgl_agenda = Agenda.objects.get(pk=single_agenda.id)
            sgl_hagenda = HistAgenda.objects.get(pk=single_agenda.id)
            sgl_hagenda.start_time_new = sgl_agenda.start_time
            sgl_hagenda.end_time_new   = sgl_agenda.end_time
            sgl_hagenda.observation = sgl_agenda.observation
            sgl_hagenda.save()

            messages.success(request, ("New data is added successfully"))
        return redirect('agenda_list')
    
    else:
        userprofile = User.objects.get(id=request.user.id)
        single_agenda= Agenda.objects.get(pk=pk)
        commentagendaform = CommentAgendaForm(instance=single_agenda)

        context = {
            'userprofile':userprofile,
            'single_agenda':single_agenda,
            'commentagendaform': commentagendaform,
        }
    return render(request, 'event/comment_agenda_add.html', context)




#======================================== List All Informative ================================================================
@login_required(login_url="/login/")
def informative_list(request):
    context = {
    }
    return render(request, 'event/informative_list.html', context)


#============================================= Informative Add ================================================================
@login_required(login_url='login')
def informative_add(request):
    if not request.user.is_authenticated :
        return redirect('login')

    if request.method == "POST":
        informativeform = InformativeForm(request.POST)
        if informativeform.is_valid():
            informativeform = informativeform.save(commit=False)
            informativeform.user=request.user
            informativeform.save()
            messages.success(request, ("New data is added successfully"))
        return redirect('informative_list')
    else:
        userprofile = User.objects.get(id=request.user.id)
        informativeform = InformativeForm()
        context = {
            'userprofile':userprofile,
            'informativeform': informativeform,
        }
    return render(request, 'event/informative_add.html', context)

#============================================= Agenda Edit ================================================================
@login_required(login_url='login')
def informative_edit(request,pk):
    if not request.user.is_authenticated :
        return redirect('login')

    if request.method == "POST":
        single_informative = Informative.objects.get(pk=pk)
        informativeform = InformativeForm(request.POST, request.FILES, instance=single_informative)
        if informativeform.is_valid():
            informativeform.save()
        messages.success(request, ("Dadus  hadia ona"))
        return redirect('informative_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_informative= Informative.objects.get(pk=pk)
        informativeform = InformativeForm(instance=single_informative)

        context = {
        'userprofile':userprofile,
        'single_informative': single_informative,
        'informativeform': informativeform,
        }
        return render(request, 'event/informative_edit.html', context)

#============================================= Agenda Delete ================================================================
@login_required(login_url='login')
def informative_delete(request,pk):

    single_informative = Informative.objects.get(id=pk)
    single_informative.delete()
    messages.success(request, ("Data is deleted successfully"))
    return redirect('informative_list')



#================================================= Concluded ================================================================
@login_required(login_url="/login/")
def concludedInformative_list(request):
    context = {
    }
    return render(request, 'event/concluded_informative.html', context)

@login_required(login_url="/login/")
def concludedInformative_list_detail(request, title_slug):
    if not request.user.is_authenticated :
        return redirect('login')

    single_informative = Informative.objects.get(title_slug=title_slug)
    multiple_comment = CommentInformative.objects.filter(informative__title_slug=title_slug)
    multiple_comment_count =multiple_comment.count()
    userprofile = User.objects.get(id=request.user.id)

    context = {
            'userprofile':userprofile,
            'single_informative':single_informative,
            'multiple_comment':multiple_comment,
            'multiple_comment_count':multiple_comment_count,
        }

    return render(request, 'event/concluded_informative_detail.html', context)

@login_required(login_url="/login/")
def unexecutedInformative_list(request):
    context = {
    }
    return render(request, 'event/unexecuted_informative.html', context)


#============================================= Comment Informative Add ================================================================
@login_required(login_url='login')
def commentinformative_add(request, pk):
    if not request.user.is_authenticated :
        return redirect('login')

    #single_informative = request.POST.get('informative_id')
    single_informative = Informative.objects.get(id=pk)

    if request.method == "POST":
        commentinformativeform = CommentInformativeForm(request.POST)
        if commentinformativeform.is_valid():
            commentinformativeform = commentinformativeform.save(commit=False)
            commentinformativeform.informative=single_informative
            commentinformativeform.is_active=True
            commentinformativeform.save()
            messages.success(request, ("New data is added successfully"))
        return redirect('concludedInformative_list')
    else:
        commentinformativeform = CommentInformativeForm()
        context = {
            'single_informative':single_informative,
            'commentinformativeform': commentinformativeform,
        }
    return render(request, 'event/comment_informative_add.html', context)
