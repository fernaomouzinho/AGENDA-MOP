from django.utils import timezone
from django.urls import reverse
from agendaapps.authentication.decorators import allowed_users
from agenda.utils import get_roles

from agendaapps.event.models import (
    Agenda,
    AgendaDelegation,
    HistAgenda,
    Yearagenda,
    RequestAgenda,
    Informative,
)

from agendaapps.institute.models import (
    Institution,
    Attendence,
    unitADN,
    DepartmentADN,
)

from agendaapps.event.models import (
    Notification,
    NotificationRead,
)

from agendaapps.event.services import (
    get_notifications_for_roles,
)


@allowed_users( allowed_roles=['sii_admin','ajenda_admin','ajenda_user','ajenda_vmn'])
def menu_home(request):

    roles = get_roles(request)

    if not isinstance(roles, (list, tuple)):
        roles = []

    roles = list(roles)

    current_datetime = timezone.now()


    # =========================================================
    # VICE MINISTER
    # =========================================================
    if "ajenda_vmn" in roles:

        delegation_list = list(
            AgendaDelegation.objects
            .filter(
                delegated_to__code="VMN"
            )
            .select_related(
                "agenda",
                "agenda__catagenda",
                "agenda__meeting_type",
                "agenda__institution",
                "delegated_from",
                "delegated_to"
            )
            .order_by(
                "-agenda__start_time"
            )
        )


        # =====================================================
        # COUNTERS
        # =====================================================
        total_count = 0
        upcoming_count = 0
        running_count = 0
        concluded_count = 0


        # =====================================================
        # NEXT DELEGATION
        # =====================================================
        next_delegation = None


        # =====================================================
        # CALENDAR
        # =====================================================
        delegation_calendar_events = []


        # =====================================================
        # PROCESS DELEGATION
        # =====================================================
        for obj in delegation_list:

            agenda = obj.agenda

            total_count += 1


            # -------------------------------------------------
            # UPCOMING
            # -------------------------------------------------
            if current_datetime < agenda.start_time:

                obj.meeting_status = "Upcoming"
                obj.meeting_status_label = "TUIR MAI"

                upcoming_count += 1

                if (
                    next_delegation is None
                    or
                    agenda.start_time
                    <
                    next_delegation.agenda.start_time
                ):

                    next_delegation = obj


            # -------------------------------------------------
            # RUNNING
            # -------------------------------------------------
            elif (
                agenda.start_time
                <= current_datetime
                <= agenda.end_time
            ):

                obj.meeting_status = "Running"
                obj.meeting_status_label = "LAO HELA"

                running_count += 1


            # -------------------------------------------------
            # CONCLUDED
            # -------------------------------------------------
            else:

                obj.meeting_status = "Concluded"
                obj.meeting_status_label = "KONKLUIDU"

                concluded_count += 1


            # -------------------------------------------------
            # CALENDAR URL
            # -------------------------------------------------
            detail_url = reverse(
                "agenda_delegation_detail",
                kwargs={
                    "uuid": obj.uuid
                }
            )


            # -------------------------------------------------
            # CALENDAR
            # -------------------------------------------------
            delegation_calendar_events.append({

                "id":
                    str(obj.uuid),

                "title":
                    agenda.title,

                "start":
                    agenda.start_time.isoformat(),

                "end":
                    agenda.end_time.isoformat(),

                "url":
                    detail_url,

                "status":
                    obj.meeting_status,

                "status_label":
                    obj.meeting_status_label,

                "delegated_from":
                    (
                        obj.delegated_from.name
                        if obj.delegated_from
                        else ""
                    ),

                "delegated_to":
                    (
                        obj.delegated_to.name
                        if obj.delegated_to
                        else ""
                    ),

                "location":
                    agenda.location or "",

                "institution":
                    (
                        str(agenda.institution)
                        if agenda.institution
                        else ""
                    ),

                "category":
                    (
                        str(agenda.catagenda)
                        if agenda.catagenda
                        else ""
                    ),

                "meeting_type":
                    (
                        str(agenda.meeting_type)
                        if agenda.meeting_type
                        else ""
                    ),

                "note":
                    obj.note or "",
            })


        # =====================================================
        # RETURN VICE MINISTER CONTEXT
        # =====================================================
        return {

            "roles":
                roles,

            "current_datetime":
                current_datetime,

            "is_vice_minister":
                True,

            "delegation_list":
                delegation_list,

            "total_count":
                total_count,

            "upcoming_count":
                upcoming_count,

            "running_count":
                running_count,

            "concluded_count":
                concluded_count,

            "next_delegation":
                next_delegation,

            "calendar_events":
                delegation_calendar_events,
        }


    # =========================================================
    # OTHER ROLES
    # sii_admin / ajenda_admin / ajenda_user
    # =========================================================
    else:

        institution_list = (
            Institution.objects
            .all()
            .order_by(
                "name_institution"
            )
        )

        attendence_list = (
            Attendence.objects.all()
        )

        unit_list = (
            unitADN.objects.all()
        )

        dep_list = (
            DepartmentADN.objects.all()
        )


        # =====================================================
        # BASE AGENDA
        # =====================================================
        agenda_list = (
            Agenda.objects
            .filter(
                is_active=True,
                status="Read"
            )
            .select_related(
                "catagenda",
                "meeting_type",
                "institution"
            )
        )


        agenda_list_home = (
            agenda_list
            .order_by(
                "is_cancel",
                "-start_time"
            )
        )


        # =====================================================
        # DASHBOARD - HIDE CANCELLED
        # =====================================================
        agenda_dashboard_list = (
            agenda_list
            .filter(
                is_cancel=False
            )
            .order_by(
                "-start_time"
            )
        )

        agenda_dashboard_count = (
            agenda_dashboard_list.count()
        )


        # =====================================================
        # ACTIVE DELEGATION
        # =====================================================
        active_delegations = (
            AgendaDelegation.objects
            .filter(
                is_active=True
            )
            .select_related(
                "agenda",
                "delegated_from",
                "delegated_to"
            )
            .order_by(
                "-delegated_at"
            )
        )


        active_delegation_map = {}

        for delegation in active_delegations:

            if (
                delegation.agenda_id
                not in active_delegation_map
            ):

                active_delegation_map[
                    delegation.agenda_id
                ] = delegation


        # =====================================================
        # UPCOMING
        # =====================================================
        upcoming_dashboard_agendas = (
            agenda_dashboard_list
            .filter(
                start_time__gt=current_datetime
            )
            .order_by(
                "start_time"
            )
        )


        # =====================================================
        # NEXT MINISTER / VICE MINISTER
        # =====================================================
        next_minister_agenda = None
        next_vice_agenda = None


        for agenda in upcoming_dashboard_agendas:

            active_delegation = (
                active_delegation_map.get(
                    agenda.id
                )
            )

            agenda.active_delegation = (
                active_delegation
            )


            if (
                active_delegation
                and
                active_delegation.delegated_to
                and
                active_delegation.delegated_to.code == "VMN"
            ):

                if next_vice_agenda is None:

                    next_vice_agenda = agenda

            else:

                if next_minister_agenda is None:

                    next_minister_agenda = agenda


            if (
                next_minister_agenda
                and
                next_vice_agenda
            ):
                break


        # =====================================================
        # CALENDAR
        # =====================================================
        calendar_events = []


        # =====================================================
        # PROCESS AGENDA
        # =====================================================
        for obj in agenda_dashboard_list:

            obj.active_delegation = (
                active_delegation_map.get(
                    obj.id
                )
            )


            # -------------------------------------------------
            # UPCOMING
            # -------------------------------------------------
            if obj.start_time > current_datetime:

                obj.meeting_status = "Upcoming"
                obj.meeting_status_label = "TUIR MAI"

                difference = (
                    obj.start_time
                    -
                    current_datetime
                )

                detail_url = reverse(
                    "upcomingAgenda_list_detail",
                    kwargs={
                        "title_slug":
                            obj.title_slug
                    }
                )


            # -------------------------------------------------
            # RUNNING
            # -------------------------------------------------
            elif (
                obj.start_time
                <= current_datetime
                and
                obj.end_time
                >= current_datetime
            ):

                obj.meeting_status = "Running"
                obj.meeting_status_label = "LAO HELA"

                difference = (
                    obj.end_time
                    -
                    current_datetime
                )

                detail_url = reverse(
                    "runningAgenda_list_detail",
                    kwargs={
                        "title_slug":
                            obj.title_slug
                    }
                )


            # -------------------------------------------------
            # CONCLUDED
            # -------------------------------------------------
            else:

                obj.meeting_status = "Concluded"
                obj.meeting_status_label = "KONKLUIDU"

                difference = None

                detail_url = reverse(
                    "concludedAgenda_list_detail",
                    kwargs={
                        "title_slug":
                            obj.title_slug
                    }
                )


            # =================================================
            # COUNTDOWN
            # =================================================
            if difference:

                total_seconds = max(
                    0,
                    int(
                        difference.total_seconds()
                    )
                )

                days = (
                    total_seconds // 86400
                )

                remaining_seconds = (
                    total_seconds % 86400
                )

                hours = (
                    remaining_seconds // 3600
                )

                remaining_seconds = (
                    remaining_seconds % 3600
                )

                minutes = (
                    remaining_seconds // 60
                )

                parts = []

                if days > 0:
                    parts.append(
                        f"Loron {days}"
                    )

                if hours > 0:
                    parts.append(
                        f"Oras {hours}"
                    )

                if minutes > 0:
                    parts.append(
                        f"Minutu {minutes}"
                    )


                if obj.meeting_status == "Upcoming":

                    obj.tempu_atu_enkontru = (
                        "Hela "
                        +
                        " ".join(parts)
                        if parts
                        else "Menus Minutu 1"
                    )

                else:

                    obj.tempu_atu_enkontru = (
                        "Remata iha "
                        +
                        " ".join(parts)
                        if parts
                        else "Besik remata"
                    )

            else:

                obj.tempu_atu_enkontru = (
                    "Remata ona"
                )


            # =================================================
            # DELEGATION
            # =================================================
            is_delegated = False
            delegated_from = ""
            delegated_to = ""
            delegation_note = ""


            if obj.active_delegation:

                is_delegated = True

                if obj.active_delegation.delegated_from:

                    delegated_from = (
                        obj.active_delegation
                        .delegated_from
                        .name
                    )

                if obj.active_delegation.delegated_to:

                    delegated_to = (
                        obj.active_delegation
                        .delegated_to
                        .name
                    )

                delegation_note = (
                    obj.active_delegation.note
                    or ""
                )


            # =================================================
            # CALENDAR EVENT
            # =================================================
            calendar_events.append({

                "id":
                    str(obj.uuid),

                "title":
                    obj.title,

                "start":
                    obj.start_time.isoformat(),

                "end":
                    obj.end_time.isoformat(),

                "url":
                    detail_url,

                "status":
                    obj.meeting_status,

                "status_label":
                    obj.meeting_status_label,

                "category":
                    (
                        str(obj.catagenda)
                        if obj.catagenda
                        else ""
                    ),

                "meeting_type":
                    (
                        str(obj.meeting_type)
                        if obj.meeting_type
                        else ""
                    ),

                "institution":
                    (
                        str(obj.institution)
                        if obj.institution
                        else ""
                    ),

                "location":
                    obj.location or "",

                "is_delegated":
                    is_delegated,

                "delegated_from":
                    delegated_from,

                "delegated_to":
                    delegated_to,

                "delegation_note":
                    delegation_note,
            })


        # =====================================================
        # STATUS QUERYSETS
        # =====================================================
        concluded_agenda = (
            agenda_dashboard_list
            .filter(
                end_time__lt=current_datetime
            )
            .order_by(
                "start_time"
            )
        )

        concluded_agenda_count = (
            concluded_agenda.count()
        )


        running_agenda = (
            agenda_dashboard_list
            .filter(
                start_time__lte=current_datetime,
                end_time__gte=current_datetime
            )
            .order_by(
                "start_time"
            )
        )

        running_agenda_count = (
            running_agenda.count()
        )


        upcoming_agenda = (
            agenda_dashboard_list
            .filter(
                start_time__gt=current_datetime
            )
            .order_by(
                "start_time"
            )
        )

        upcoming_agenda_count = (
            upcoming_agenda.count()
        )


        # =====================================================
        # OTHER CONTEXT
        # =====================================================
        histori_agenda_list = (
            HistAgenda.objects
            .filter(
                is_active=True
            )
        )

        all_year = (
            Yearagenda.objects
            .all()
            .order_by(
                "-year"
            )
        )

        request_agenda_list = (
            RequestAgenda.objects.all()
        )

        informative_list = (
            Informative.objects
            .filter(
                is_active=True
            )
        )

        informative_count = (
            informative_list.count()
        )


        # =====================================================
        # RETURN NORMAL CONTEXT
        # =====================================================
        return {

            "roles":
                roles,

            "is_vice_minister":
                False,

            "current_datetime":
                current_datetime,

            "institution_list":
                institution_list,

            "attendence_list":
                attendence_list,

            "unit_list":
                unit_list,

            "dep_list":
                dep_list,

            "agenda_list":
                agenda_list,

            "agenda_list_home":
                agenda_list_home,

            "agenda_dashboard_list":
                agenda_dashboard_list,

            "agenda_dashboard_count":
                agenda_dashboard_count,

            "concluded_agenda":
                concluded_agenda,

            "concluded_agenda_count":
                concluded_agenda_count,

            "running_agenda":
                running_agenda,

            "running_agenda_count":
                running_agenda_count,

            "upcoming_agenda":
                upcoming_agenda,

            "upcoming_agenda_count":
                upcoming_agenda_count,

            "next_minister_agenda":
                next_minister_agenda,

            "next_vice_agenda":
                next_vice_agenda,

            "calendar_events":
                calendar_events,

            "histori_agenda_list":
                histori_agenda_list,

            "all_year":
                all_year,

            "request_agenda_list":
                request_agenda_list,

            "informative_list":
                informative_list,

            "informative_count":
                informative_count,
        }
        

def notification_context(request):

    # =====================================================
    # CURRENT USER
    # =====================================================

    user_id = (
        getattr(
            request,
            "portal_user_id",
            None
        )
        or
        request.session.get(
            "agenda_user_id"
        )
    )

    roles = (
        getattr(
            request,
            "portal_roles",
            None
        )
        or
        request.session.get(
            "agenda_roles",
            []
        )
        or
        []
    )


    # =====================================================
    # SAFE EMPTY CONTEXT
    # =====================================================

    if (
        not user_id
        or
        not roles
    ):

        return {

            "header_notifications":
                [],

            "unread_notification_count":
                0,
        }


    user_id = str(
        user_id
    )


    # =====================================================
    # ROLE-SPECIFIC NOTIFICATION
    # =====================================================

    notifications = (
        get_notifications_for_roles(
            roles
        )
    )


    # =====================================================
    # READ IDS FOR CURRENT USER
    # =====================================================

    read_ids = set(

        NotificationRead.objects
        .filter(
            central_user_id=user_id
        )
        .values_list(
            "notification_id",
            flat=True
        )
    )


    # =====================================================
    # UNREAD
    # =====================================================

    unread_notification_count = (
        notifications
        .exclude(
            id__in=read_ids
        )
        .count()
    )


    # =====================================================
    # LATEST 10
    # =====================================================

    header_notifications = list(
        notifications[:10]
    )


    # Template property
    for notification in header_notifications:

        notification.user_has_read = (
            notification.id
            in
            read_ids
        )


    return {

        "header_notifications":
            header_notifications,

        "unread_notification_count":
            unread_notification_count,
    }