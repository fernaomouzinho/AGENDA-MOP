from django.urls import reverse

from .models import (
    Notification,
    AgendaDelegation,
)


# ============================================================
# SSO USER
# ============================================================

def get_request_sso_user(request):

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
        or
        ""
    )

    username = (
        getattr(
            request,
            "portal_user",
            None
        )
        or
        request.session.get(
            "agenda_user"
        )
        or
        ""
    )

    return (
        str(user_id),
        username
    )


# ============================================================
# IS AGENDA DELEGATED TO VMN?
# ============================================================

def agenda_is_delegated_to_vmn(agenda):

    return (
        AgendaDelegation.objects
        .filter(
            agenda=agenda,
            is_active=True,
            delegated_to__code="VMN"
        )
        .exists()
    )


# ============================================================
# CURRENT RESPONSIBLE ROLE
# ============================================================

def get_agenda_responsible_role(agenda):

    if agenda_is_delegated_to_vmn(
        agenda
    ):
        return "ajenda_vmn"

    return "ajenda_user"


# ============================================================
# GENERIC CREATE NOTIFICATION
# ============================================================

def create_notification(
    *,
    request=None,
    agenda=None,
    recipient_role,
    notification_type,
    title,
    message,
    url=None,
):

    created_by_user_id = ""
    created_by_username = ""

    if request:

        (
            created_by_user_id,
            created_by_username
        ) = get_request_sso_user(
            request
        )

    return Notification.objects.create(

        recipient_role=
            recipient_role,

        notification_type=
            notification_type,

        title=
            title,

        message=
            message,

        agenda=
            agenda,

        url=
            url,

        created_by_user_id=
            created_by_user_id,

        created_by_username=
            created_by_username,
    )


# ============================================================
# AGENDA NEW
#
# Always for Minister.
# ============================================================

def notify_new_agenda(
    request,
    agenda
):

    agenda_url = reverse(
        "upcomingAgenda_list_detail",
        kwargs={
            "title_slug":
                agenda.title_slug
        }
    )

    return create_notification(

        request=request,

        agenda=agenda,

        recipient_role=
            "ajenda_user",

        notification_type=
            "AGENDA_NEW",

        title=
            "Ajenda Foun",

        message=(
            f'Ajenda "{agenda.title}" '
            f'rejista ona. '
            f'Data: '
            f'{agenda.start_time.strftime("%d/%m/%Y %H:%M")}.'
        ),

        url=
            agenda_url,
    )


# ============================================================
# AGENDA UPDATED
#
# Not delegated -> Minister
# Delegated     -> Vice Minister
# ============================================================

def notify_agenda_updated(
    request,
    agenda
):

    recipient_role = (
        get_agenda_responsible_role(
            agenda
        )
    )

    agenda_url = reverse(
        "upcomingAgenda_list_detail",
        kwargs={
            "title_slug":
                agenda.title_slug
        }
    )

    return create_notification(

        request=request,

        agenda=agenda,

        recipient_role=
            recipient_role,

        notification_type=
            "AGENDA_UPDATE",

        title=
            "Ajenda Atualizadu",

        message=(
            f'Ajenda "{agenda.title}" '
            f'atualiza ona. '
            f'Favor haree informasaun foun.'
        ),

        url=
            agenda_url,
    )


# ============================================================
# DELEGATION
#
# Always for Vice Minister.
# ============================================================

def notify_delegation(
    request,
    delegation
):

    agenda = (
        delegation.agenda
    )

    delegation_url = reverse(
        "agenda_delegation_detail",
        kwargs={
            "uuid":
                delegation.uuid
        }
    )

    return create_notification(

        request=request,

        agenda=agenda,

        recipient_role=
            "ajenda_vmn",

        notification_type=
            "DELEGATION",

        title=
            "Delegasaun Ajenda",

        message=(
            f'Ajenda "{agenda.title}" '
            f'delega ba '
            f'{delegation.delegated_to.name}.'
        ),

        url=
            delegation_url,
    )


# ============================================================
# REMINDER
#
# Not delegated -> Minister
# Delegated     -> Vice Minister
# ============================================================

def notify_agenda_reminder(
    agenda,
    message
):

    recipient_role = (
        get_agenda_responsible_role(
            agenda
        )
    )

    agenda_url = reverse(
        "upcomingAgenda_list_detail",
        kwargs={
            "title_slug":
                agenda.title_slug
        }
    )

    return create_notification(

        agenda=agenda,

        recipient_role=
            recipient_role,

        notification_type=
            "REMINDER",

        title=
            "Reminder Ajenda",

        message=
            message,

        url=
            agenda_url,
    )
    

# ============================================================
# NOTIFICATIONS ALLOWED FOR CURRENT ROLE
# ============================================================

def get_notifications_for_roles(
    roles
):

    if not roles:

        return (
            Notification.objects.none()
        )


    # ========================================================
    # VICE MINISTER
    # ========================================================

    if "ajenda_vmn" in roles:

        return (
            Notification.objects
            .filter(
                recipient_role="ajenda_vmn",
                notification_type__in=[
                    "DELEGATION",
                    "AGENDA_UPDATE",
                    "REMINDER",
                ]
            )
            .select_related(
                "agenda"
            )
            .order_by(
                "-created_at"
            )
        )


    # ========================================================
    # MINISTER
    # ========================================================

    if "ajenda_user" in roles:

        return (
            Notification.objects
            .filter(
                recipient_role="ajenda_user",
                notification_type__in=[
                    "AGENDA_NEW",
                    "AGENDA_UPDATE",
                    "REMINDER",
                ]
            )
            .select_related(
                "agenda"
            )
            .order_by(
                "-created_at"
            )
        )


    return (
        Notification.objects.none()
    )