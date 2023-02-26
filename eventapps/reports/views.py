from django.shortcuts import render
import csv
from django.http import HttpResponse
from eventapps.event.models import Agenda
from datetime import datetime

# Create your views here.
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
