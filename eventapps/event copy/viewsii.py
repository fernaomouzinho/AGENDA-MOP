from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Agenda
from .form import AgendaForm
from django.contrib.auth.models import User

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
            agendaform = agendaform.save()
            messages.success(request, ("Dadus foun aumenta ona"))
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
        single_agenda = Event.objects.get(pk=pk)
        agendaform = AgendaForm(request.POST, request.FILES, instance=single_agenda)
        if agendaform.is_valid():
            agendaform.save()
        messages.success(request, ("Dadus  hadia ona"))
        return redirect('agenda_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_agenda= Event.objects.get(pk=pk)
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
    
    single_agenda = Event.objects.get(id=pk)
    single_agenda.delete()
    messages.success(request, ("Delete successfully"))
    return redirect('agenda_list')




    
#======================================== Completed ================================================================
@login_required(login_url="/login/")
def completed_view(request):
    context = {
    }
    return render(request, 'event/completed_agenda.html', context)

@login_required(login_url="/login/")
def completed_view_detail(request, title_slug):
    single_agenda = Event.objects.get(title_slug=title_slug)
    context = {
        'single_agenda':single_agenda,
    }
    return render(request, 'event/completed_agenda_detail.html', context)

#======================================== Canceled ================================================================

@login_required(login_url="/login/")
def canceled_view(request):
    context = {
    }
    return render(request, 'event/canceled_agenda.html', context)

@login_required(login_url="/login/")
def canceled_view_detail(request):
    context = {
    }
    return render(request, 'event/canceled_agenda_detail.html', context)

#========================================= Running ================================================================
@login_required(login_url="/login/")
def running_view(request):
    context = {
    }
    return render(request, 'event/running_agenda.html', context)

@login_required(login_url="/login/")
def running_view_detail(request, title_slug):
    context = {
    }
    return render(request, 'event/running_agenda_detail.html', context)

#======================================== Upcoming ================================================================
@login_required(login_url="/login/")
def upcoming_view(request):
    context = {
    }
    return render(request, 'event/upcoming_agenda.html', context)


@login_required(login_url="/login/")
def upcoming_view_detail(request, title_slug):
    context = {
    }
    return render(request, 'event/upcoming_agenda_detail.html', context)


@login_required(login_url="/login/")
def upcoming_edit(request, pk):
    single_agenda = Event.objects.get(id=pk)
    context = {
        'single_agenda':single_agenda,
    }
    return render(request, 'event/upcoming_agenda_edit.html', context)    

@login_required(login_url='login')
def upcoming_delete(request,pk):
    
    single_agenda = Event.objects.get(id=pk)
    single_agenda.delete()
    messages.success(request, ("Dadus hamos ona"))
    return redirect('upcoming_view')

@login_required(login_url='login')
def upcoming_cancel(request,pk):
  
    single_agenda = Event.objects.get(id=pk)
    single_agenda.is_cancel = "True"
    single_agenda.save()
    return redirect('upcoming_view')

    
#======================================== Postpone ================================================================
@login_required(login_url="/login/")
def postpone_view(request):
    context = {
    }
    return render(request, 'event/postpone_agenda.html', context)


