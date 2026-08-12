import urllib.parse

# 👉 SIMPLE (no API required)
def generate_whatsapp_link(phone, message):
    encoded = urllib.parse.quote(message)
    return f"https://wa.me/{phone}?text={encoded}"


def build_agenda_message(agenda):
    return f"""
📅 AJENDA FOUN

📌 Titulu: {agenda.title}
🏢 Instituisaun: {agenda.institution}
📍 Fatin: {agenda.location}

⏰ Hahu: {agenda.start_time.strftime('%d-%m-%Y %H:%M')}
⏰ Remata: {agenda.end_time.strftime('%d-%m-%Y %H:%M')}

📝 Observasaun:
{agenda.observation or '-'}
"""