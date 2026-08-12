from django.shortcuts import render
from django.shortcuts import render, redirect
import csv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from agendaapps.event.models import CatAgenda, Agenda, Yearagenda
from datetime import datetime
from .form import CalendarPickerForm,AgendaSearchForm
from agendaapps.reports.models import Semestral, Trimestral, Mensual
import os
from pathlib import Path
# from reportlab.pdfgen    import canvas
# from reportlab.lib.utils import ImageReader
# from datetime            import datetime



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


#======================================= ANUAL ========================================#
@login_required(login_url="/login/")
def report_based_anual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    current_datetime = datetime.now()
    anual_report = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime).order_by('-start_time')

    context = {
        'single_year':single_year,
        'anual_report':anual_report,
    }
    return render(request, 'report/report_annual.html', context)


#=================================== SEMESTRAL ========================================#
# Semestral Annual
@login_required(login_url="/login/")
def report_based_semestral(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)

    context = {
        'single_year':single_year,
    }
    return render(request, 'report/report_semestral.html', context)

# Semestral Annual Detail
@login_required(login_url="/login/")
def report_based_semestral_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()


    month_start = 1
    month_end = 6

    a = request.path
    print(a)
    b = Path(a)
    c=b.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/"+d+"/semestral/first-semester/":
        rs=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end).order_by('-start_time')
    else:
        rs=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'semester_report':rs,
    }
    return render(request, 'report/report_semestral_detail.html', context)

# Semestral Category
@login_required(login_url="/login/")
def report_based_semestral_category_detail(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    month_start = 1
    month_end = 6

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/"+d+"/semestral/first-semester/internal/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/first-semester/external/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/second-semester/internal/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/second-semester/external/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'single_category':single_category,
        'semester_cat_report':rsc,
    }
    return render(request, 'report/report_semestral_category_detail.html', context)


# Semestral Concluded
@login_required(login_url="/login/")
def report_based_semestral_concluded_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()

    month_start = 1
    month_end = 6
    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]
    if a == "/report/"+d+"/semestral/first-semester/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/second-semester/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, is_cancel=False).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'semester_cat_concluded_report':rscc,
    }
    return render(request, 'report/report_semestral_concluded_detail.html', context)


# Semestral Category Concluded
@login_required(login_url="/login/")
def report_based_semestral_canceled_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()
    month_start = 1
    month_end = 6
    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)

    if a == "/report/"+d+"/semestral/first-semester/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/second-semester/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, is_cancel=True).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'semester_cat_report':rsc,
    }
    return render(request, 'report/report_semestral_canceled_detail.html', context)


# Semestral category Concluded
@login_required(login_url="/login/")
def report_based_semestral_category_concluded_detail(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    month_start = 1
    month_end = 6
    a = request.path
    b = Path(a)
    c=b.parent.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]


    if a == "/report/"+d+"/semestral/first-semester/internal/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/first-semester/external/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/second-semester/internal/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/second-semester/external/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'single_category':single_category,
        'semester_cat_concluded_report':rscc,
    }
    return render(request, 'report/report_semestral_category_concluded_detail.html', context)

# Semestral Category Canceled
@login_required(login_url="/login/")
def report_based_semestral_category_canceled_detail(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    month_start = 1
    month_end = 6

    a = request.path
    print(a)
    b = Path(a)
    c=b.parent.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)

    if a == "/report/"+d+"/semestral/first-semester/internal/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/first-semester/external/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/second-semester/internal/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/semestral/second-semester/external/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'single_category':single_category,
        'semester_cat_report':rsc,
    }
    return render(request, 'report/report_semestral_category_canceled_detail.html', context)


#======================================= TRIMESTRAL ========================================#
# Trimestral Annual
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
    current_datetime = datetime.now()

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
    head_tail = os.path.split(a)
    v = head_tail[0]

    if v == "/report/"+d+"/trimestral/first-trimester":
        rt=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end).order_by('-start_time')
    elif v == "/report/"+d+"/trimestral/second-trimester":
        rt=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end).order_by('-start_time')
    elif v == "/report/"+d+"/trimestral/third-trimester":
        rt=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end).order_by('-start_time')
    elif v == "/report/"+d+"/trimestral/fourth-trimester":
        rt=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'trimester_report':rt,
    }
    return render(request, 'report/report_trimestral_detail.html', context)


# Trimestral Category
@login_required(login_url="/login/")
def report_based_trimestral_category_detail(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/"+d+"/trimestral/first-trimester/internal/":
        rtc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/second-trimester/internal/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/third-trimester/internal/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/fourth-trimester/internal/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/first-trimester/external/":
        rtc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/second-trimester/external/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/third-trimester/external/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/fourth-trimester/external/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'single_category':single_category,
        'trimester_cat_report':rtc,
    }
    return render(request, 'report/report_trimestral_category_detail.html', context)

# Trimestral Concluded
@login_required(login_url="/login/")
def report_based_trimestral_concluded_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/"+d+"/trimestral/first-trimester/concluded/":
        rtcc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/second-trimester/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/third-trimester/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/fourth-trimester/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, is_cancel=False).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'trimester_cat_report':rtcc,
    }
    return render(request, 'report/report_trimestral_concluded_detail.html', context)


# Trimestral Canceled
@login_required(login_url="/login/")
def report_based_trimestral_canceled_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/"+d+"/trimestral/first-trimester/canceled/":
        rtcc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/second-trimester/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/third-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/fourth-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, is_cancel=True).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'trimester_cat_report':rtcc,
    }
    return render(request, 'report/report_trimestral_canceled_detail.html', context)


# Trimestral Category Concluded
@login_required(login_url="/login/")
def report_based_trimestral_category_concluded_detail(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]
    print(a)

    if a == "/report/"+d+"/trimestral/first-trimester/internal/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/second-trimester/internal/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/third-trimester/internal/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/fourth-trimester/internal/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/first-trimester/external/concluded/":
        rtcc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/second-trimester/external/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/third-trimester/external/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/fourth-trimester/external/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'single_category':single_category,
        'trimester_cat_concluded_report':rtcc,
    }
    return render(request, 'report/report_trimestral_category_concluded_detail.html', context)

# Trimestral Category Canceled
@login_required(login_url="/login/")
def report_based_trimestral_category_canceled_detail(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/"+d+"/trimestral/first-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/second-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/third-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/fourth-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/first-trimester/external/canceled/":
        rtcc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/second-trimester/external/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/third-trimester/external/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/"+d+"/trimestral/fourth-trimester/external/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'single_category':single_category,
        'trimester_cat_report':rtcc,
    }
    return render(request, 'report/report_trimestral_category_canceled_detail.html', context)


#=================================== MENSAL ======================================#
#Mensal Anual
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

#Mensal Anual Detail
@login_required(login_url="/login/")
def report_based_mensual_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    current_datetime = datetime.now()

    report_mensual = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'report_mensual':report_mensual,
    }
    return render(request, 'report/report_mensual_detail.html', context)


#Mensal Concluded
@login_required(login_url="/login/")
def report_based_mensual_concluded_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    current_datetime = datetime.now()

    report_mensual_concluded = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num, is_cancel=False)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'report_mensual_concluded':report_mensual_concluded,
    }
    return render(request, 'report/report_mensual_concluded_detail.html', context)


#Mensal Canceled
@login_required(login_url="/login/")
def report_based_mensual_canceled_detail(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    current_datetime = datetime.now()

    report_mensual_canceled = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num, is_cancel=True)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'report_mensual_canceled':report_mensual_canceled,
    }
    return render(request, 'report/report_mensual_canceled_detail.html', context)

#Mensal Category
@login_required(login_url="/login/")
def report_based_mensual_category_detail(request, year, name_slug, name_cat_slug ):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    report_mensual_category = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num, catagenda__name_category_slug=name_cat_slug)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'single_category':single_category,
        'report_mensual_category':report_mensual_category,
    }
    return render(request, 'report/report_mensual_category_detail.html', context)


#Mensal Category
@login_required(login_url="/login/")
def report_based_mensual_category_concluded_detail(request, year, name_slug, name_cat_slug ):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    report_mensual_cat_concluded = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num, catagenda__name_category_slug=name_cat_slug, is_cancel=False)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'single_category':single_category,
        'report_mensual_cat_concluded':report_mensual_cat_concluded,
    }
    return render(request, 'report/report_mensual_category_concluded_detail.html', context)


#Mensal Category
@login_required(login_url="/login/")
def report_based_mensual_category_canceled_detail(request, year, name_slug, name_cat_slug ):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    report_mensual_cat_canceled = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num, catagenda__name_category_slug=name_cat_slug, is_cancel=True)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'single_category':single_category,
        'report_mensual_cat_canceled':report_mensual_cat_canceled,
    }
    return render(request, 'report/report_mensual_category_canceled_detail.html', context)


# Category Annual
@login_required(login_url="/login/")
def report_based_catagenda_annual(request, year, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()
    report_catagenda_anual = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_category':single_category,
        'report_catagenda_anual':report_catagenda_anual,
    }
    return render(request, 'report/report_catagenda_annual.html', context)

#Concluded Annual
@login_required(login_url="/login/")
def report_based_concludedagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')

    current_datetime = datetime.now()
    single_year = Yearagenda.objects.get(year=year)
    report_concludedagenda_anual = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, is_cancel=False).order_by('-start_time')

    context = {
        'single_year':single_year,
        'report_concludedagenda_anual':report_concludedagenda_anual,
    }
    return render(request, 'report/report_concludedagenda_annual.html', context)

#Canceled Annual
@login_required(login_url="/login/")
def report_based_canceledagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')

    single_year = Yearagenda.objects.get(year=year)
    report_canceledagenda_anual = Agenda.objects.filter(start_time__year=year, is_cancel=True).order_by('-start_time')

    context = {
        'single_year':single_year,
        'report_canceledagenda_anual':report_canceledagenda_anual,
    }
    return render(request, 'report/report_canceledagenda_annual.html', context)

@login_required(login_url="/login/")
def report_based_upcomingagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')

    single_year = Yearagenda.objects.get(year=year)
    report_upcomingagenda_anual = Agenda.objects.filter(is_active=True, is_cancel=False, status='Read', start_time__year=year, start_time__gte=datetime.now()).order_by("start_time")

    context = {
        'single_year':single_year,
        'report_upcomingagenda_anual':report_upcomingagenda_anual,
    }
    return render(request, 'report/report_upcomingagenda_annual.html', context)



#=================================== DAILY ======================================#
#Daily
@login_required(login_url="/login/")
def report_based_daily(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = AgendaSearchForm(request.GET)
    agendas = Agenda.objects.filter(is_active=True, status='Read', is_cancel=False,  end_time__lt=datetime.now()).order_by("start_time")
    
    
    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        if start_date:
            agendas = agendas.filter(start_time__date__gte=start_date)
        if end_date:
            agendas = agendas.filter(end_time__date__lte=end_date)

    context = {
        'form':form,
        'agendas':agendas,
        
    }
    return render(request, 'report/report_daily.html', context)




#===================================================== PRINT REPORT ================================================
# Report all Agenda Anual except upcoming agenda
@login_required(login_url="/login/")
def print_all_reportagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    current_datetime = datetime.now()
    anual_report = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime).order_by('-start_time')

    context = {
       'single_year':single_year,
       'anual_report':anual_report,
    }
    return render(request, 'report/print/print_all_reportagenda_annual.html', context)

# Report all Agenda based Semestre except upcoming agenda
@login_required(login_url="/login/")
def print_all_reportagenda_semestral(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()


    month_start = 1
    month_end = 6

    a = request.path
    b = Path(a)
    c=b.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/agenda/"+d+"/semestral/first-semester/":
        rs=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/second-semester/":
        rs=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'semester_report':rs,
    }
    return render(request, 'report/print/print_all_reportagenda_semestral.html', context)


# Report all Agenda based Semestre except upcoming agenda
@login_required(login_url="/login/")
def print_all_reportagenda_semestral_concluded(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()

    month_start = 1
    month_end = 6

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]


    if a == "/report/agenda/"+d+"/semestral/first-semester/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/second-semester/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, is_cancel=False).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'semester_concluded_report':rscc,
    }
    return render(request, 'report/print/print_all_reportagenda_semestral_concluded.html', context)

# Report all Agenda based Semestre except upcoming agenda
@login_required(login_url="/login/")
def print_all_reportagenda_semestral_canceled(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()

    month_start = 1
    month_end = 6

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)

    if a == "/report/agenda/"+d+"/semestral/first-semester/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/second-semester/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, is_cancel=True).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'semester_canceled_report':rsc,
    }
    return render(request, 'report/print/print_all_reportagenda_semestral_canceled.html', context)


# Trimestral Category
@login_required(login_url="/login/")
def print_all_reportagenda_semestral_category(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    month_start = 1
    month_end = 6

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]


    if a == "/report/agenda/"+d+"/semestral/first-semester/internal/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/first-semester/external/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/second-semester/internal/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/second-semester/external/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'single_category':single_category,
        'semester_cat_report':rsc,
    }
    return render(request, 'report/print/print_all_reportagenda_semestral_category.html', context)

# Trimestral Category
@login_required(login_url="/login/")
def print_all_reportagenda_semestral_category_concluded(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    month_start = 1
    month_end = 6

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]


    if a == "/report/agenda/"+d+"/semestral/first-semester/internal/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/first-semester/external/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/second-semester/internal/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/second-semester/external/concluded/":
        rscc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'single_category':single_category,
        'semester_cat_concluded_report':rscc,
    }
    return render(request, 'report/print/print_all_reportagenda_semestral_category_concluded.html', context)


# Trimestral Category
@login_required(login_url="/login/")
def print_all_reportagenda_semestral_category_canceled(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_semester=Semestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    month_start = 1
    month_end = 6

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)


    if a == "/report/agenda/"+d+"/semestral/first-semester/internal/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/first-semester/external/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=month_start, start_time__month__lte=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/second-semester/internal/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/semestral/second-semester/external/canceled/":
        rsc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=month_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')


    context = {
        'single_year':single_year,
        'single_semester':single_semester,
        'single_category':single_category,
        'semester_cat_canceled_report':rsc,
    }
    return render(request, 'report/print/print_all_reportagenda_semestral_category_canceled.html', context)


#================================= Report all Agenda based Trimester except upcoming agenda =================
# Print Report Trimestral
@login_required(login_url="/login/")
def print_all_reportagenda_trimestral(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()

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
        rt=Agenda.objects.filter(start_time__month__gte=firstPeriode_start, end_time__lt=current_datetime, start_time__month__lte=firstPeriode_end).order_by('-start_time')
    elif v == "/report/agenda/"+d+"/trimestral/second-trimester":
        rt=Agenda.objects.filter(start_time__month__gte=secondPeriode_start, end_time__lt=current_datetime, start_time__month__lte=secondPeriode_end).order_by('-start_time')
    elif v == "/report/agenda/"+d+"/trimestral/third-trimester":
        rt=Agenda.objects.filter(start_time__year=year, start_time__month__gte=thirdPeriode_start, end_time__lt=current_datetime, start_time__month__lte=thirdPeriode_end).order_by('-start_time')
    elif v == "/report/agenda/"+d+"/trimestral/fourth-trimester":
        rt=Agenda.objects.filter(start_time__year=year, start_time__month__gt=thirdPeriode_end, end_time__lt=current_datetime).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'trimester_report':rt,
    }
    return render(request, 'report/print/print_all_reportagenda_trimestral.html', context)


# Print Report Trimestral Concluded
@login_required(login_url="/login/")
def print_all_reportagenda_trimestral_concluded(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/agenda/"+d+"/trimestral/first-trimester/concluded/":
        rtcc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/second-trimester/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/third-trimester/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/fourth-trimester/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, is_cancel=False).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'trimester_concluded_report':rtcc,
    }
    return render(request, 'report/print/print_all_reportagenda_trimestral_concluded.html', context)

# Print Report Trimestral Concluded
@login_required(login_url="/login/")
def print_all_reportagenda_trimestral_canceled(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    current_datetime = datetime.now()

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/agenda/"+d+"/trimestral/first-trimester/canceled/":
        rtcc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/second-trimester/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/third-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/fourth-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, is_cancel=True).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'trimester_canceled_report':rtcc,
    }
    return render(request, 'report/print/print_all_reportagenda_trimestral_canceled.html', context)

# Print Report Trimestral Category
@login_required(login_url="/login/")
def print_all_reportagenda_trimestral_category(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/agenda/"+d+"/trimestral/first-trimester/internal/":
        rtc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/second-trimester/internal/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/third-trimester/internal/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/fourth-trimester/internal/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/first-trimester/external/":
        rtc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/second-trimester/external/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/third-trimester/external/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/fourth-trimester/external/":
        rtc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'single_category':single_category,
        'trimester_cat_report':rtc,
    }
    return render(request, 'report/print/print_all_reportagenda_trimestral_category.html', context)

# Print Report Trimestral Category Concluded
@login_required(login_url="/login/")
def print_all_reportagenda_trimestral_category_concluded(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/agenda/"+d+"/trimestral/first-trimester/internal/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
        print(rtcc)
    elif a == "/report/agenda/"+d+"/trimestral/second-trimester/internal/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/third-trimester/internal/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/fourth-trimester/internal/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/first-trimester/external/concluded/":
        rtcc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/second-trimester/external/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/third-trimester/external/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/fourth-trimester/external/concluded/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=False).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'single_category':single_category,
        'trimester_cat_concluded_report':rtcc,
    }
    return render(request, 'report/print/print_all_reportagenda_trimestral_category_concluded.html', context)

# Print Report Trimestral Category Canceled
@login_required(login_url="/login/")
def print_all_reportagenda_trimestral_category_canceled(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_trimester=Trimestral.objects.get(name_slug=name_slug)
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    firstPeriode_start = 1
    firstPeriode_end = 3
    secondPeriode_start = 4
    secondPeriode_end = 6
    thirdPeriode_start = 7
    thirdPeriode_end = 9

    a = request.path
    b = Path(a)
    c=b.parent.parent.parent.parent
    d=c.stem
    head_tail = os.path.split(a)
    v = head_tail[0]

    if a == "/report/agenda/"+d+"/trimestral/first-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/second-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/third-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/fourth-trimester/internal/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/first-trimester/external/canceled/":
        rtcc=Agenda.objects.filter( start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=firstPeriode_start, start_time__month__lte=firstPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/second-trimester/external/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=secondPeriode_start, start_time__month__lte=secondPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/third-trimester/external/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gte=thirdPeriode_start, start_time__month__lte=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')
    elif a == "/report/agenda/"+d+"/trimestral/fourth-trimester/external/canceled/":
        rtcc=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month__gt=thirdPeriode_end, catagenda__name_category_slug=name_cat_slug, is_cancel=True).order_by('-start_time')

    context = {
        'single_year':single_year,
        'single_trimester':single_trimester,
        'single_category':single_category,
        'trimester_cat_canceled_report':rtcc,
    }
    return render(request, 'report/print/print_all_reportagenda_trimestral_category_canceled.html', context)

# ==============================  Report all Agenda based Mensual except upcoming agenda ================
@login_required(login_url="/login/")
def print_all_reportagenda_mensual(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    report_mensual = Agenda.objects.filter(start_time__year=year, start_time__month=month_num)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'report_mensual':report_mensual,
    }
    return render(request, 'report/print/print_all_reportagenda_mensual.html', context)

@login_required(login_url="/login/")
def print_all_reportagenda_mensual_concluded(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    current_datetime = datetime.now()

    report_mensual_concluded = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num, is_cancel=False)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'report_mensual_concluded':report_mensual_concluded,
    }
    return render(request, 'report/print/print_all_reportagenda_mensual_concluded.html', context)

@login_required(login_url="/login/")
def print_all_reportagenda_mensual_canceled(request, year, name_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    current_datetime = datetime.now()

    report_mensual_canceled = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num, is_cancel=True)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'report_mensual_canceled':report_mensual_canceled,
    }
    return render(request, 'report/print/print_all_reportagenda_mensual_canceled.html', context)


@login_required(login_url="/login/")
def print_all_reportagenda_mensual_category(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    report_mensual_category = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num, catagenda__name_category_slug=name_cat_slug)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'single_category':single_category,
        'report_mensual_category':report_mensual_category,
    }
    return render(request, 'report/print/print_all_reportagenda_mensual_category.html', context)

@login_required(login_url="/login/")
def print_all_reportagenda_mensual_category_concluded(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    report_mensual_cat_concluded = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num, catagenda__name_category_slug=name_cat_slug, is_cancel=False)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'single_category':single_category,
        'report_mensual_cat_concluded':report_mensual_cat_concluded,
    }
    return render(request, 'report/print/print_all_reportagenda_mensual_category_concluded.html', context)

@login_required(login_url="/login/")
def print_all_reportagenda_mensual_category_canceled(request, year, name_slug, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    single_month=Mensual.objects.get(name_slug=name_slug)
    month_num = datetime.strptime(name_slug, '%B').month
    single_category = CatAgenda.objects.get(name_category_slug=name_cat_slug)
    current_datetime = datetime.now()

    report_mensual_cat_canceled = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, start_time__month=month_num, catagenda__name_category_slug=name_cat_slug, is_cancel=True)

    context = {
        'single_year':single_year,
        'single_month':single_month,
        'single_category':single_category,
        'report_mensual_cat_canceled':report_mensual_cat_canceled,
    }
    return render(request, 'report/print/print_all_reportagenda_mensual_category_canceled.html', context)

# ==============================  Report all Agenda based Category Anual except upcoming agenda ================
@login_required(login_url="/login/")
def print_all_reportagenda_category(request, year, name_cat_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    current_datetime = datetime.now()
    report_catagenda_anual = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime, catagenda__name_category_slug=name_cat_slug).order_by('-start_time')

    context = {
        'single_year':single_year,
        'report_catagenda_anual':report_catagenda_anual,
    }
    return render(request, 'report/print/print_all_reportagenda_category.html', context)



# ==============================  Report all Agenda based Concluded Anual except upcoming agenda ================
@login_required(login_url="/login/")
def print_all_reportconcludedagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    current_datetime = datetime.now()
    single_year = Yearagenda.objects.get(year=year)
    report_concludedagenda_anual = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime).order_by('-start_time')

    context = {
       'single_year':single_year,
       'report_concludedagenda_anual':report_concludedagenda_anual,
    }
    return render(request, 'report/print/print_all_reportconcludedagenda_annual.html', context)

# ==============================  Report all Agenda based Canceled Annual except upcoming agenda ================
@login_required(login_url="/login/")
def print_all_reportcanceledagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    report_canceledagenda_anual = Agenda.objects.filter(start_time__year=year, is_cancel=True).order_by('-start_time')

    context = {
       'single_year':single_year,
       'report_canceledagenda_anual':report_canceledagenda_anual,
    }
    return render(request, 'report/print/print_all_reportcanceledagenda_annual.html', context)

# ==============================  Report all Agenda based Upcoming Annual  ================
@login_required(login_url="/login/")
def print_all_reportupcomingagenda_annual(request, year):
    if not request.user.is_authenticated:
        return redirect('login')
    single_year = Yearagenda.objects.get(year=year)
    report_upcomingagenda_anual = Agenda.objects.filter(is_active=True, is_cancel=False, status='Read', start_time__year=year, start_time__gte=datetime.now()).order_by("start_time")

    context = {
       'single_year':single_year,
       'report_upcomingagenda_anual':report_upcomingagenda_anual,
    }
    return render(request, 'report/print/print_all_reportupcomingagenda_annual.html', context)

# ======================================  Report Daily Agenda  =====================================================
@login_required(login_url="/login/")
def print_each_reportagenda_daily(request, title_slug):
    if not request.user.is_authenticated:
        return redirect('login')
    
    report_daily = Agenda.objects.filter(title_slug=title_slug)

    context = {
       'report_daily':report_daily,
    }
    return render(request, 'report/print/print_each_reportagenda_daily.html', context)









#======================================================== Download CSV ===========================================================
def csv_all_reportagenda_annual(request, year):
    response = HttpResponse(content_type='text/csv')
    response['Content_Disposition'] = 'attachment; filename="agenda.csv"'
    writer=csv.writer(response)

    writer.writerow(['Relatorio Meeting Management'])
    writer.writerow(['Nu', 'Data/Loron', 'Agenda', 'Observasaun'])
    current_datetime = datetime.now()
    n=0
    anual_report=Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime).order_by('-start_time')
    for i in anual_report:
        writer.writerow([n+1, i.start_time, i.title, i.observation])
        n=n+1
    return response







#======================================================== Download PDF ===========================================================
# def pdf_all_reportagenda_annual(request, year):
#     # Create the HttpResponse object
#     response = HttpResponse(content_type='application/pdf')
#     # This line force a download
#     response['Content-Disposition'] = 'attachment; filename="1.pdf"'
#     # Generate unique timestamp
#     ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
#     p = canvas.Canvas(response)
#     # Write content on the PDF

#     my_image = ImageReader('https://www.google.com/images/srpr/logo11w.png')

#     p.drawImage(my_image, 10, 600, mask='auto')




#     current_datetime = datetime.now()
#     anual_report = Agenda.objects.filter(start_time__year=year, end_time__lt=current_datetime).order_by('-start_time')
#     p.drawString(100, 500, "a")
#     p.showPage()
#     p.save()

#     # Show the result to the user
#     return response
