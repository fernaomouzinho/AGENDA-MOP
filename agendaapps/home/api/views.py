from django.http import JsonResponse
import requests

def agenda_auth_status(request):
    session_jti = request.session.get("jwt_jti")
    session_user_id = request.session.get("jwt_user_id")
    session_version = request.session.get("jwt_session_version")
    print("dd",request.session.session_key)
    print('FERNAO',session_user_id)

    if not session_jti:
        return JsonResponse({"active": False})

    try:
        res = requests.get(
            "http://127.0.0.1:8000/api/check-session/",
            params={
                "jti": session_jti,
                "user_id": session_user_id,
                "session_version": session_version
            },
            timeout=2
        )

        if res.status_code == 200:
            return JsonResponse(res.json())

    except:
        pass

    return JsonResponse({"active": True})