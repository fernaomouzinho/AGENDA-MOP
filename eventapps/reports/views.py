from django.shortcuts import render
from django.shortcuts import render, redirect
import csv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from eventapps.event.models import Agenda
from datetime import datetime
from .form import CalendarPickerForm



# Create your views here.

@login_required(login_url="/login/")
def report_agenda(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
    }
    return render(request, 'report/report_agenda.html', context)


@login_required(login_url="/login/")
def print_all_report_agenda(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
    }
    return render(request, 'report/print_all_report_agenda.html', context)



def download_Completed_Agenda_CSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content_Disposition'] = 'attachment; filename="agenda.csv"'
    writer=csv.writer(response)
    writer.writerow(['Relatorio Meeting Management'])
    writer.writerow(['Nu', 'Data/Loron', 'Agenda', 'Observasaun'])

    n=0
    for i in Agenda.objects.all():
        writer.writerow([n+1, i.start_time, i.title, i.observation])
        n=n+1
    return response

def download_Concluded_Agenda_CSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content_Disposition'] = 'attachment; filename="agenda.csv"'
    writer=csv.writer(response)
    writer.writerow(['Relatorio Meeting Management'])
    writer.writerow(['Nu', 'Data/Loron', 'Agenda', 'Observasaun'])
    current_datetime = datetime.now()

    n=0
    for i in Agenda.objects.all():
        if i.start_time >= current_datetime:
            writer.writerow([n+1, i.start_time, i.title, i.observation])
        n=n+1
    return response

def download_Upcoming_Agenda_CSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content_Disposition'] = 'attachment; filename="agenda.csv"'
    writer=csv.writer(response)
    writer.writerow(['Relatorio Meeting Management'])
    writer.writerow(['Nu', 'Data/Loron', 'Agenda', 'Observasaun'])

    n=0
    for i in Agenda.objects.all():

        writer.writerow([n+1, i.start_time, i.title, i.observation])
        n=n+1
    return response
