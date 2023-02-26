from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Institution, Attendence
from .form import InstitutionForm, AttendenceForm
from eventapps.authentication.models import User


# Create your views here.

# ======================================== List All Institute ================================================================
@login_required(login_url="/login/")
def institution_list(request):
    context = {
    }
    return render(request, 'institute/institution_list.html', context)

# ============================================= Institute Add ================================================================


@login_required(login_url='login')
def institution_add(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        institutionform = InstitutionForm(request.POST, request.FILES)
        if institutionform.is_valid():
            institutionform = institutionform.save(commit=False)
            institutionform.user = request.user
            institutionform.save()

            messages.success(request, ("New data is added"))
        return redirect('institution_list')
    else:
        userprofile = User.objects.get(id=request.user.id)
        institutionform = InstitutionForm()
        context = {
            'userprofile': userprofile,
            'institutionform': institutionform,
        }

    return render(request, 'institute/institution_add.html', context)

# ============================================= Institute Edit ================================================================


@login_required(login_url='login')
def institution_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        single_institution = Institution.objects.get(pk=pk)
        institutionform = InstitutionForm(
            request.POST, request.FILES, instance=single_institution)
        if institutionform.is_valid():
            institutionform.save()
        messages.success(request, ("Data is updated"))
        return redirect('institution_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_institution = Institution.objects.get(pk=pk)
        institutionform = InstitutionForm(instance=single_institution)

        context = {
            'userprofile': userprofile,
            'single_institution': single_institution,
            'institutionform': institutionform,
        }
        return render(request, 'institute/institution_edit.html', context)

# ============================================= Institute Delete ================================================================


@login_required(login_url='login')
def institution_delete(request, pk):

    single_institute = Institution.objects.get(id=pk)
    single_institute.delete()
    messages.success(request, ("Delete successfully"))
    return redirect('institution_list')


# Create your views here.

# ======================================== List All Attendence ================================================================
@login_required(login_url="/login/")
def attendence_list(request):
    context = {
    }
    return render(request, 'institute/attendence_list.html', context)

# ============================================= Attendence Add ================================================================


@login_required(login_url='login')
def attendence_add(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        attendenceform = AttendenceForm(request.POST, request.FILES)
        if attendenceform.is_valid():
            attendenceform = attendenceform.save(commit=False)
            attendenceform.user = request.user
            attendenceform.save()

            messages.success(request, ("New Data Added"))
        return redirect('attendence_list')
    else:
        userprofile = User.objects.get(id=request.user.id)
        attendenceform = AttendenceForm()
        context = {
            'userprofile': userprofile,
            'attendenceform': attendenceform,
        }

    return render(request, 'institute/attendence_add.html', context)

# ============================================= Attendence Edit ================================================================


@login_required(login_url='login')
def attendence_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        single_attendence = Attendence.objects.get(pk=pk)
        attendenceform = AttendenceForm(
            request.POST, request.FILES, instance=single_attendence)
        if attendenceform.is_valid():
            attendenceform.save()
        messages.success(request, ("Dadus  hadia ona"))
        return redirect('attendence_list')

    else:
        userprofile = User.objects.get(id=request.user.id)
        single_attendence = Attendence.objects.get(pk=pk)
        attendenceform = AttendenceForm(instance=single_attendence)

        context = {
            'userprofile': userprofile,
            'single_attendence': single_attendence,
            'attendenceform': attendenceform,
        }
        return render(request, 'institute/attendence_edit.html', context)

# ============================================= Attendence Delete ================================================================


@login_required(login_url='login')
def attendence_delete(request, pk):

    single_attendence = Attendence.objects.get(id=pk)
    single_attendence.delete()
    messages.success(request, ("Delete successfully"))
    return redirect('attendence_list')
