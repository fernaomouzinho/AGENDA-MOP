from django.shortcuts import render
from django.shortcuts import render, redirect
import csv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from eventapps.event.models import CatAgenda, Agenda, Yearagenda
from datetime import datetime
from .form import CalendarPickerForm
from eventapps.reports.models import Semestral, Trimestral, Mensual
import os
from pathlib import Path



# Create your views here.

@login_required(login_url="/login/")
def report_agenda(request):
    if not request.user.is_authenticated:
        return redirect('login')
    year=datetime.now().year
    single_year = Yearagenda.objects.get(year=year)
    context = {
       'single_year':single_year,
    }

    return render(request, 'report/report_home.html', context)

@login_required(login_url="/login/")
def report_based_year(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)

    context = {
        'single_year':single_year,
    }
    return render(request, 'report/report_year.html', context)

@login_required(login_url="/login/")
def report_based_anual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    anual_report = Agenda.objects.filter(start_time__year=year).order_by('-start_time')


    context = {
        'single_year':single_year,
        'anual_report':anual_report,
    }
    return render(request, 'report/report_annual.html', context)


@login_required(login_url="/login/")
def report_based_semestral(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)


    context = {
        'single_year':single_year,
    }
    return render(request, 'report/report_semestral.html', context)


@login_required(login_url="/login/")
def report_based_semestral_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    month_start = 1
    month_end = 6

    a = request.path
    b = Path(a)
    c=b.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if v == "/report/"+d+"/semetral/first-semester":
        rs=Agenda.objects.filter(start_time__month__gte=month_start, start_time__month__lte=month_end, start_time__year=year).order_by('-start_time')
    else:
        rs=Agenda.objects.filter(start_time__month__gt=month_end)

    context = {
        'single_year':single_year,
        #'all_semesters':all_semesters,
        'single_semester':single_semester,
        'semester_report':rs,
    }
    return render(request, 'report/report_semestral_detail.html', context)


@login_required(login_url="/login/")
def report_based_trimestral(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)

    context = {
        'single_year':single_year,
    }
    return render(request, 'report/report_trimestral.html', context)


@login_required(login_url="/login/")
def report_based_trimestral_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent
    d=c.stem
    print(d)
    head_tail = os.path.split(a)
    v = head_tail[0]

    if v == "/report/"+d+"/trimestral/first-trimester":
        rt=Agenda.objects.filter(start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, start_time__year=year).order_by('-start_time')
    elif v == "/report/"+d+"/trimestral/second-trimester":
        rt=Agenda.objects.filter(start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, start_time__year=year).order_by('-start_time')
    elif v == "/report/"+d+"/trimestral/third-trimester":
        rt=Agenda.objects.filter(start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, start_time__year=year).order_by('-start_time')
    else:
        rt=Agenda.objects.filter(start_time__month__gt=thirdPeriode_end, start_time__year=year).order_by('-start_time')


    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'trimester_report':rt,
    }
    return render(request, 'report/report_trimestral_detail.html', context)



@login_required(login_url="/login/")
def report_based_mensual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    all_months=Mensual.objects.all()

    context = {
        'single_year':single_year,
        'all_months':all_months,
    }
    return render(request, 'report/report_mensual.html', context)


@login_required(login_url="/login/")
def report_based_mensual_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    #all_trimesters=Trimestral.objects.all()
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    report_mensual = Agenda.objects.filter(start_time__month=month_num)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'report_mensual':report_mensual,
    }
    return render(request, 'report/report_mensual_detail.html', context)




@login_required(login_url="/login/")
def report_based_catagenda_annual(request, year, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    report_catagenda_anual = Agenda.objects.filter(catagenda__name_category_slug=name_cat_slug, start_time__year=year).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_category':single_category,
        'report_catagenda_anual':report_catagenda_anual,
    }
    return render(request, 'report/report_catagenda_annual.html', context)

@login_required(login_url="/login/")
def report_based_concludedagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')

    current_datetime = datetime.now()
    single_year = Yearagenda.objects.get(year=year)
    report_concludedagenda_anual = Agenda.objects.filter(end_time__lt=current_datetime, start_time__year=year).order_by('-start_time')


    context = {
        'single_year':single_year,
        'report_concludedagenda_anual':report_concludedagenda_anual,
    }
    return render(request, 'report/report_concludedagenda_annual.html', context)


@login_required(login_url="/login/")
def report_based_canceledagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')

    single_year = Yearagenda.objects.get(year=year)
    report_canceledagenda_anual = Agenda.objects.filter(is_cancel=True, start_time__year=year).order_by('-start_time')


    context = {
        'single_year':single_year,
        'report_canceledagenda_anual':report_canceledagenda_anual,
    }
    return render(request, 'report/report_canceledagenda_annual.html', context)



























@login_required(login_url="/login/")
def print_all_reportagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    context = {
       'single_year':single_year,
    }
    return render(request, 'report/print/print_all_reportagenda_annual.html', context)

@login_required(login_url="/login/")
def print_all_reportagenda_semestral(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    month_start = 1
    month_end = 6

    a = request.path
    b = Path(a)
    c=b.parent
    print(c)
    d=c.stem
    print(d)
    head_tail = os.path.split(a)
    v = head_tail[0]

    if v == "/report/agenda/"+d+"/first-semester":
        rs=Agenda.objects.filter(start_time__month__gte=month_start, start_time__month__lte=month_end, start_time__year=year).order_by('-start_time')
    else:
        rs=Agenda.objects.filter(start_time__month__gt=month_end)

    context = {
        'single_year':single_year,
        #'all_semesters':all_semesters,
        'single_semester':single_semester,
        'semester_report':rs,
    }
    return render(request, 'report/print/print_all_reportagenda_semestral.html', context)



@login_required(login_url="/login/")
def print_all_reportagenda_trimestral(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent
    d=c.stem
    print(d)
    head_tail = os.path.split(a)
    v = head_tail[0]

    if v == "/report/agenda/"+d+"/trimestral/first-trimester":
        rt=Agenda.objects.filter(start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, start_time__year=year).order_by('-start_time')
    elif v == "/report/agenda/"+d+"/trimestral/second-trimester":
        rt=Agenda.objects.filter(start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, start_time__year=year).order_by('-start_time')
    elif v == "/report/agenda/"+d+"/trimestral/third-trimester":
        rt=Agenda.objects.filter(start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, start_time__year=year).order_by('-start_time')
    else:
        rt=Agenda.objects.filter(start_time__month__gt=thirdPeriode_end, start_time__year=year).order_by('-start_time')


    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'trimester_report':rt,
    }
    return render(request, 'report/print/print_all_reportagenda_trimestral.html', context)


@login_required(login_url="/login/")
def print_all_reportagenda_mensual(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    report_mensual = Agenda.objects.filter(start_time__month=month_num)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'report_mensual':report_mensual,
    }
    return render(request, 'report/print/print_all_reportagenda_mensual.html', context)










@login_required(login_url="/login/")
def print_all_reportagenda_category(request, year, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    report_catagenda_anual = Agenda.objects.filter(catagenda__name_category_slug=name_cat_slug, start_time__year=year).order_by('-start_time')

    context = {
        'single_year':single_year,
        'report_catagenda_anual':report_catagenda_anual,
    }
    return render(request, 'report/print/print_all_reportagenda_category.html', context)


@login_required(login_url="/login/")
def print_all_reportconcludedagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    current_datetime = datetime.now()
    single_year = Yearagenda.objects.get(year=year)
    report_concludedagenda_anual = Agenda.objects.filter(end_time__lt=current_datetime, start_time__year=year).order_by('-start_time')

    context = {
       'single_year':single_year,
       'report_concludedagenda_anual':report_concludedagenda_anual,
    }
    return render(request, 'report/print/print_all_reportconcludedagenda_annual.html', context)

@login_required(login_url="/login/")
def print_all_reportcanceledagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    report_canceledagenda_anual = Agenda.objects.filter(is_cancel=True, start_time__year=year).order_by('-start_time')

    context = {
       'single_year':single_year,
       'report_canceledagenda_anual':report_canceledagenda_anual,
    }
    return render(request, 'report/print/print_all_reportcanceledagenda_annual.html', context)


















































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
