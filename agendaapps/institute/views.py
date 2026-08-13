from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Institution, Attendence
from .form import InstitutionForm, AttendenceForm
from agendaapps.authentication.models import User
from agendaapps.authentication.decorators import allowed_users
from agenda.utils import get_roles


# Create your views here.
# ======================================== List All Institute ================================================================
@allowed_users(allowed_roles=['ajenda_admin'])
def institution_list(request):
    roles = get_roles(request)
    context = {
        'roles': roles
    }
    return render(request, 'institute/institution_list.html', context)

# ============================================= Institute Add ================================================================

@allowed_users(allowed_roles=['ajenda_admin'])
def institution_add(request):
    roles = get_roles(request)

    if request.method == "POST":
        institutionform = InstitutionForm(request.POST, request.FILES)
        if institutionform.is_valid():
            institutionform = institutionform.save(commit=False)
            institutionform.save()

            messages.success(request, ("Dadus foun rejista ho susesu."))
        return redirect('institution_list')
    else:
        institutionform = InstitutionForm()
        context = {
            'institutionform': institutionform,
            'roles': roles
        }

    return render(request, 'institute/institution_add.html', context)

# ============================================= Institute Edit ================================================================


@allowed_users(allowed_roles=['ajenda_admin'])
def institution_edit(request, uuid):

    roles = get_roles(request)

    single_institution = get_object_or_404(
        Institution,
        uuid=uuid
    )

    if request.method == "POST":

        institutionform = InstitutionForm(
            request.POST,
            request.FILES,
            instance=single_institution
        )

        if institutionform.is_valid():

            institutionform.save()

            messages.success(
                request,
                f'Instituisaun "{single_institution.name_institution}" '
                f'atualiza ho susesu.'
            )

            return redirect(
                'institution_list'
            )

    else:

        institutionform = InstitutionForm(
            instance=single_institution
        )

    context = {
        'single_institution': single_institution,
        'institutionform': institutionform,
        'roles': roles,
    }

    return render(
        request,
        'institute/institution_edit.html',
        context
    )



# ============================================= Institute Delete ================================================================

@allowed_users(allowed_roles=['ajenda_admin'])
def institution_delete(request, uuid):

    roles = get_roles(request)

    single_institution = get_object_or_404(
        Institution,
        uuid=uuid
    )

    if request.method == "POST":

        # Save name before deleting
        institution_name = single_institution.name_institution

        # Delete institution
        single_institution.delete()

        # Success message in Tetun
        messages.success(
            request,
            f'Instituisaun "{institution_name}" hamos ho susesu.'
        )

        return redirect(
            'institution_list'
        )

    context = {
        'single_institution': single_institution,
        'roles': roles,
    }

    return render(
        request,
        'institute/institution_delete.html',
        context
    )

# Create your views here.

# ======================================== List All Attendence ================================================================
@allowed_users(allowed_roles=['ajenda_admin'])
def attendence_list(request):
    roles = get_roles(request)
    context = {
        'roles': roles
    }
    return render(request, 'institute/attendence_list.html', context)

# ============================================= Attendence Add ================================================================


@allowed_users(allowed_roles=['ajenda_admin'])
def attendence_add(request):
    roles = get_roles(request)

    if request.method == "POST":
        attendenceform = AttendenceForm(request.POST, request.FILES)
        if attendenceform.is_valid():
            attendenceform = attendenceform.save(commit=False)
            attendenceform.save()

            messages.success(request, ("New Data Added"))
        return redirect('attendence_list')
    else:
        attendenceform = AttendenceForm()
        context = {
            'attendenceform': attendenceform,
            'roles': roles
        }

    return render(request, 'institute/attendence_add.html', context)

# ============================================= Attendence Edit ================================================================

@allowed_users(allowed_roles=['ajenda_admin'])
def attendence_edit(request, pk):
    roles = get_roles(request)
    if request.method == "POST":
        single_attendence = Attendence.objects.get(pk=pk)
        attendenceform = AttendenceForm(
            request.POST, request.FILES, instance=single_attendence)
        if attendenceform.is_valid():
            attendenceform.save()
        messages.success(request, ("Dadus  hadia ona"))
        return redirect('attendence_list')

    else:
        single_attendence = Attendence.objects.get(pk=pk)
        attendenceform = AttendenceForm(instance=single_attendence)

        context = {
            'single_attendence': single_attendence,
            'attendenceform': attendenceform,
            'roles': roles
        }
        return render(request, 'institute/attendence_edit.html', context)

# ============================================= Attendence Delete ================================================================

@allowed_users(allowed_roles=['ajenda_admin'])
def attendence_delete(request, pk):
    roles = get_roles(request)
    single_attendence = Attendence.objects.get(id=pk)
    single_attendence.delete()
    messages.success(request, ("Delete successfully"))
    return redirect('attendence_list')
