from agendaapps.event.models import CatAgenda, Agenda, RequestAgenda, HistAgenda, Yearagenda, Informative, CommentInformative
from agendaapps.institute.models import Institution, Attendence, unitADN, DepartmentADN
from agendaapps.reports.models import Semestral, Trimestral, Mensual, Logo
from datetime import datetime
from django.db.models import Count
from django.utils import timezone


def menu_home(request):
    current_datetime = timezone.now()
    institution_list = Institution.objects.all().order_by("name_institution")
    attendence_list = Attendence.objects.all()
    unit_list = unitADN.objects.all()
    dep_list = DepartmentADN.objects.all()

    agenda_list = Agenda.objects.filter(is_active=True, status='Read')
    histori_agenda_list = HistAgenda.objects.filter(is_active=True)
    agenda_list_home = agenda_list.order_by('is_cancel', '-start_time')
    agenda_count = agenda_list.count()
    
    
    # ==========================================
    # TEMPU ATU ENKONTRU - TETUM
    # ==========================================
    for obj in agenda_list_home:

        # UPCOMING
        if obj.start_time > current_datetime:

            difference = obj.start_time - current_datetime

            total_seconds = int(
                difference.total_seconds()
            )

            days = total_seconds // 86400

            remaining_seconds = (
                total_seconds % 86400
            )

            hours = remaining_seconds // 3600

            remaining_seconds = (
                remaining_seconds % 3600
            )

            minutes = remaining_seconds // 60

            parts = []

            if days > 0:
                parts.append(
                    f"Hela Loron {days}"
                )

            if hours > 0:
                parts.append(
                    f" Oras {hours}"
                )

            if minutes > 0:
                parts.append(
                    f" Minutu {minutes}"
                )

            if parts:
                obj.tempu_atu_enkontru = (
                    " ".join(parts)
                )
            else:
                obj.tempu_atu_enkontru = (
                    "Menus Minutu 1"
                )


        # RUNNING
        elif (
            obj.start_time <= current_datetime
            and
            obj.end_time >= current_datetime
        ):

            difference = (
                obj.end_time - current_datetime
            )

            total_seconds = int(
                difference.total_seconds()
            )

            hours = total_seconds // 3600

            remaining_seconds = (
                total_seconds % 3600
            )

            minutes = remaining_seconds // 60

            parts = []

            if hours > 0:
                parts.append(
                    f" Oras {hours}"
                )

            if minutes > 0:
                parts.append(
                    f" Minutu {minutes}"
                )

            if parts:
                obj.tempu_atu_enkontru = (
                    "Remata iha "
                    + " ".join(parts)
                )
            else:
                obj.tempu_atu_enkontru = (
                    "Besik remata"
                )


        # FINISHED
        else:

            obj.tempu_atu_enkontru = (
                "Remata ona"
            )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    all_year = Yearagenda.objects.all().order_by('-year')
    count_agenda_in_year = agenda_list.values('start_time__year').order_by('start_time__year').annotate(count=Count('start_time__year'))

    concluded_agenda = Agenda.objects.filter(is_active=True, status='Read', is_cancel=False,  end_time__lt=datetime.now()).order_by("start_time")
    concluded_agenda_count = concluded_agenda.count()

    running_agenda = Agenda.objects.filter(is_active=True, status='Read', start_time__lte=datetime.now(), end_time__gte=datetime.now()).order_by("start_time")
    running_agenda_count = running_agenda.count()

    upcoming_agenda = Agenda.objects.filter(is_active=True, is_cancel=False, status='Read', start_time__gte=datetime.now()).order_by("start_time")
    upcoming_agenda_count = upcoming_agenda.count()
    pending_upcoming = Agenda.objects.filter(is_active=True, is_cancel=False, status='Pending', start_time__gte=datetime.now()).order_by("start_time")
    approved_upcoming = Agenda.objects.filter(is_active=True, is_cancel=False, status='Pending', start_time__gte=datetime.now()).order_by("start_time")

    canceled_agenda = Agenda.objects.filter(is_active=True, status='Read', is_cancel=True).order_by('-updated_at')
    canceled_agenda_count = canceled_agenda.count()

    request_agenda_list = RequestAgenda.objects.all()
    request_waitting = request_agenda_list.filter(is_active="False")

  
    request_approved = request_agenda_list.filter(is_active="True")

   

    pending_request = RequestAgenda.objects.filter(
        status='Pending').order_by("created_at")

    informative_list = Informative.objects.filter(is_active=True)
    informative_count = informative_list.count()

    executed_informative = Informative.objects.filter(is_active=True, is_done=True)
    executed_informative_count = executed_informative.count()
    comment_informative = CommentInformative.objects.all()

    unexecuted_informative = Informative.objects.filter(is_active=True, is_done=False)

    unexecuted_informative_count = unexecuted_informative.count()
    #current_datetime = datetime.now()
    
    
    # ======================== NOTIFICATION ========================

    # ======================== NOTIFICATION ========================

    notification_queryset = Agenda.objects.filter(
        is_active=True,
        is_cancel=False,
        status='Pending'
    )

    notification_count = notification_queryset.count()

    notification_agenda = notification_queryset.order_by(
        '-created_at'
    )[:10]

    #======================== PRINT ========================================
    all_catagenda = CatAgenda.objects.all()
    all_semesters=Semestral.objects.all()
    all_trimesters=Trimestral.objects.all()
    report_conclude = Agenda.objects.filter(is_active=True, status='Read', is_cancel=False, observation__isnull=False, end_time__lt=datetime.now()).order_by("start_time")
    logo_adn = Logo.objects.filter().last()
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
               
                pending_request=pending_request,




                informative_list=informative_list,
                informative_count=informative_count,
                executed_informative=executed_informative,
                executed_informative_count=executed_informative_count,
                comment_informative=comment_informative,
                unexecuted_informative=unexecuted_informative,
                unexecuted_informative_count=unexecuted_informative_count,
                current_datetime=current_datetime,
                
                all_catagenda=all_catagenda,
                all_semesters=all_semesters,
                all_trimesters=all_trimesters,
                report_conclude=report_conclude,
                logo_adn=logo_adn,
                
                notification_agenda=notification_agenda,
                notification_count=notification_count
                )
