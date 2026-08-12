from django.shortcuts import redirect
from agenda.utils import get_roles

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            roles = get_roles(request)
            if not roles:
                return redirect("http://localhost:5173/login")
            if any(role in allowed_roles for role in roles):
                return view_func(request, *args, **kwargs)
            return redirect("http://localhost:5173/login")
        return wrapper
    return decorator