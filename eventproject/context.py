from eventapps.event.models import Agenda, RequestAgenda, HistAgenda, Yearagenda, Informative, CommentInformative
from eventapps.institute.models import Institution, Attendence, unitADN, DepartmentADN
from datetime import datetime
from django.db.models import Count


def menu_home(request):
    institution_list = Institution.objects.all().order_by("name_institution")
    attendence_list = Attendence.objects.all()
    unit_list = unitADN.objects.all()
    dep_list = DepartmentADN.objects.all()

    agenda_list = Agenda.objects.filter(is_active=True, status='Read')
    histori_agenda_list = HistAgenda.objects.filter(is_active=True)
    agenda_list_home = agenda_list.order_by('is_cancel', '-start_time')
    agenda_count = agenda_list.count()
    all_year = Yearagenda.objects.filter(is_active=True)
    count_agenda_in_year = agenda_list.values('start_time__year').order_by(
        'start_time__year').annotate(count=Count('start_time__year'))

    concluded_agenda = Agenda.objects.filter(
        is_active=True, status='Read', is_cancel=False,  end_time__lt=datetime.now()).order_by("start_time")
    concluded_agenda_count = concluded_agenda.count()

    running_agenda = Agenda.objects.filter(is_active=True, status='Read', start_time__lte=datetime.now(
    ), end_time__gte=datetime.now()).order_by("start_time")
    running_agenda_count = running_agenda.count()

    upcoming_agenda = Agenda.objects.filter(
        is_active=True, is_cancel=False, status='Read', start_time__gte=datetime.now()).order_by("start_time")
    upcoming_agenda_count = upcoming_agenda.count()
    pending_upcoming = Agenda.objects.filter(
        is_active=True, is_cancel=False, status='Pending', start_time__gte=datetime.now()).order_by("start_time")
    approved_upcoming = Agenda.objects.filter(
        is_active=True, is_cancel=False, status='Pending', start_time__gte=datetime.now(), user=request.user).order_by("start_time")

    canceled_agenda = Agenda.objects.filter(
        is_active=True, status='Read', is_cancel=True).order_by('-updated_at')
    canceled_agenda_count = canceled_agenda.count()

    request_agenda_list = RequestAgenda.objects.all()
    request_agenda_list_user = request_agenda_list.filter(
        user=request.user.id)
    request_waitting = request_agenda_list.filter(is_active="False")

    count_wait_adj = request_waitting.filter(user__is_adj='True')
    count_wait_uga = request_waitting.filter(user__is_uga='True')
    count_wait_uap = request_waitting.filter(user__is_uap='True')
    count_wait_ucvq = request_waitting.filter(user__is_ucvq='True')
    count_wait_uedc = request_waitting.filter(user__is_uedc='True')

    request_approved = request_agenda_list.filter(is_active="True")

    count_aprv_adj = request_approved.filter(user__is_adj='True')
    count_aprv_uga = request_approved.filter(user__is_uga='True')
    count_aprv_uap = request_approved.filter(user__is_uap='True')
    count_aprv_ucvq = request_approved.filter(user__is_ucvq='True')
    count_aprv_uedc = request_approved.filter(user__is_uedc='True')

    pending_request = RequestAgenda.objects.filter(
        status='Pending').order_by("created_at")

    informative_list = Informative.objects.filter(is_active=True)
    informative_count = informative_list.count()

    executed_informative = Informative.objects.filter(
        is_active=True, is_done=True)
    executed_informative_count = executed_informative.count()
    comment_informative = CommentInformative.objects.all()

    unexecuted_informative = Informative.objects.filter(
        is_active=True, is_done=False)

    unexecuted_informative_count = unexecuted_informative.count()
    current_datetime = datetime.now()

    return dict(institution_list=institution_list,
                attendence_list=attendence_list,
                unit_list=unit_list,
                dep_list=dep_list,

                agenda_list=agenda_list,
                histori_agenda_list=histori_agenda_list,
                agenda_list_home=agenda_list_home,

                agenda_count=agenda_count,
                all_year=all_year,
                count_agenda_in_year=count_agenda_in_year,
                concluded_agenda=concluded_agenda,
                concluded_agenda_count=concluded_agenda_count,
                running_agenda=running_agenda,
                running_agenda_count=running_agenda_count,
                upcoming_agenda=upcoming_agenda,
                upcoming_agenda_count=upcoming_agenda_count,
                pending_upcoming=pending_upcoming,
                approved_upcoming=approved_upcoming,
                canceled_agenda=canceled_agenda,
                canceled_agenda_count=canceled_agenda_count,

                request_agenda_list=request_agenda_list,
                request_waitting=request_waitting,
                count_wait_adj=count_wait_adj,
                count_wait_uga=count_wait_uga,
                count_wait_uap=count_wait_uap,
                count_wait_ucvq=count_wait_ucvq,
                count_wait_uedc=count_wait_uedc,

                request_approved=request_approved,
                request_agenda_list_user=request_agenda_list_user,
                count_aprv_adj=count_aprv_adj,
                count_aprv_uga=count_aprv_uga,
                count_aprv_uap=count_aprv_uap,
                count_aprv_ucvq=count_aprv_ucvq,
                count_aprv_uedc=count_aprv_uedc,

                pending_request=pending_request,




                informative_list=informative_list,
                informative_count=informative_count,
                executed_informative=executed_informative,
                executed_informative_count=executed_informative_count,
                comment_informative=comment_informative,
                unexecuted_informative=unexecuted_informative,
                unexecuted_informative_count=unexecuted_informative_count,
                current_datetime=current_datetime,
                )
