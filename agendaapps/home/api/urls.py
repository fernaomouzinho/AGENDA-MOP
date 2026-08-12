from django.urls import path
from .views import agenda_auth_status

urlpatterns = [
	path("agenda-auth-status/", agenda_auth_status),
]