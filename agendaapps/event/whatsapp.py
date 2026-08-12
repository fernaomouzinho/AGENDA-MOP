import requests

from django.conf import settings


class WhatsAppError(Exception):
    pass


# ============================================================
# CLEAN PHONE NUMBER
# ============================================================

def clean_phone_number(
    phone_number
):

    if not phone_number:
        raise WhatsAppError(
            "Phone number is empty."
        )

    clean_number = "".join(
        character
        for character in str(phone_number)
        if character.isdigit()
    )

    if not clean_number:

        raise WhatsAppError(
            "Invalid phone number."
        )

    return clean_number


# ============================================================
# SEND WHATSAPP TEMPLATE
# ============================================================

def send_whatsapp_template(
    phone_number,
    recipient_name,
    agenda_title,
    meeting_date,
    start_time,
    end_time,
    location,
    institution,
    reminder_text,
):

    # ========================================================
    # SETTINGS
    # ========================================================

    access_token = getattr(
        settings,
        "WHATSAPP_ACCESS_TOKEN",
        None
    )

    phone_number_id = getattr(
        settings,
        "WHATSAPP_PHONE_NUMBER_ID",
        None
    )

    api_version = getattr(
        settings,
        "WHATSAPP_API_VERSION",
        None
    )

    template_name = getattr(
        settings,
        "WHATSAPP_TEMPLATE_NAME",
        None
    )

    template_language = getattr(
        settings,
        "WHATSAPP_TEMPLATE_LANGUAGE",
        "en"
    )

    # ========================================================
    # VALIDATE CONFIGURATION
    # ========================================================

    if not access_token:

        raise WhatsAppError(
            "WHATSAPP_ACCESS_TOKEN is not configured."
        )

    if not phone_number_id:

        raise WhatsAppError(
            "WHATSAPP_PHONE_NUMBER_ID is not configured."
        )

    if not api_version:

        raise WhatsAppError(
            "WHATSAPP_API_VERSION is not configured."
        )

    if not template_name:

        raise WhatsAppError(
            "WHATSAPP_TEMPLATE_NAME is not configured."
        )

    # ========================================================
    # PHONE
    # ========================================================

    phone_number = clean_phone_number(
        phone_number
    )

    # ========================================================
    # API URL
    # ========================================================

    url = (
        f"https://graph.facebook.com/"
        f"{api_version}/"
        f"{phone_number_id}/messages"
    )

    # ========================================================
    # HEADERS
    # ========================================================

    headers = {

        "Authorization": (
            f"Bearer {access_token}"
        ),

        "Content-Type": (
            "application/json"
        ),
    }

    # ========================================================
    # TEMPLATE PAYLOAD
    # ========================================================

    payload = {

        "messaging_product": (
            "whatsapp"
        ),

        "recipient_type": (
            "individual"
        ),

        "to": phone_number,

        "type": "template",

        "template": {

            "name": template_name,

            "language": {
                "code": template_language
            },

            "components": [

                {
                    "type": "body",

                    "parameters": [

                        {
                            "type": "text",
                            "text": str(
                                recipient_name
                            ),
                        },

                        {
                            "type": "text",
                            "text": str(
                                agenda_title
                            ),
                        },

                        {
                            "type": "text",
                            "text": str(
                                meeting_date
                            ),
                        },

                        {
                            "type": "text",
                            "text": str(
                                start_time
                            ),
                        },

                        {
                            "type": "text",
                            "text": str(
                                end_time
                            ),
                        },

                        {
                            "type": "text",
                            "text": str(
                                location
                            ),
                        },

                        {
                            "type": "text",
                            "text": str(
                                institution
                            ),
                        },

                        {
                            "type": "text",
                            "text": str(
                                reminder_text
                            ),
                        },

                    ],
                }

            ],
        },
    }

    # ========================================================
    # SEND REQUEST
    # ========================================================

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30,
        )

    except requests.Timeout as exc:

        raise WhatsAppError(
            "WhatsApp API request timed out."
        ) from exc

    except requests.ConnectionError as exc:

        raise WhatsAppError(
            "Cannot connect to WhatsApp API."
        ) from exc

    except requests.RequestException as exc:

        raise WhatsAppError(
            f"WhatsApp request error: {exc}"
        ) from exc

    # ========================================================
    # RESPONSE
    # ========================================================

    try:

        response_data = (
            response.json()
        )

    except ValueError:

        response_data = {
            "raw_response": (
                response.text
            )
        }

    # ========================================================
    # ERROR FROM META
    # ========================================================

    if not response.ok:

        raise WhatsAppError(
            f"WhatsApp API error "
            f"{response.status_code}: "
            f"{response_data}"
        )

    return response_data