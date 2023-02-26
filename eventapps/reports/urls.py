from django.urls import path
from . import views


urlpatterns = [
    path('completed-agenda/download/csv/', views.download_Completed_Agenda_CSV, name='download_Completed_Agenda_CSV'),
    path('concluded-agenda/download/csv/', views.download_Concluded_Agenda_CSV, name='download_Concluded_Agenda_CSV'),
    path('upcoming-agenda/download/csv/', views.download_Upcoming_Agenda_CSV, name='download_Upcoming_Agenda_CSV'),
    
]