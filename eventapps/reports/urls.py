from django.urls import path
from . import views


urlpatterns = [
    path('report/', views.report_agenda, name='report_agenda'),
    path('report/all/agenda/', views.print_all_report_agenda, name='print_all_report_agenda'),
    path('completed-agenda/download/csv/', views.download_Completed_Agenda_CSV, name='download_Completed_Agenda_CSV'),
    path('concluded-agenda/download/csv/', views.download_Concluded_Agenda_CSV, name='download_Concluded_Agenda_CSV'),
    path('upcoming-agenda/download/csv/', views.download_Upcoming_Agenda_CSV, name='download_Upcoming_Agenda_CSV'),

]
