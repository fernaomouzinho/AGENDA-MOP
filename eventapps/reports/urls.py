from django.urls import path
from . import views


urlpatterns = [
    path('report/', views.report_agenda, name='report_agenda'),
    path('report/<int:year>/', views.report_based_year, name='report_based_year'),
    path('report/<int:year>/anual/list', views.report_based_anual, name='report_based_anual'),
    path('report/<int:year>/semetral/', views.report_based_semestral, name='report_based_semestral'),
    path('report/<int:year>/semetral/<slug:name_slug>/', views.report_based_semestral_detail, name='report_based_semestral_detail'),
    path('report/<int:year>/trimestral/', views.report_based_trimestral, name='report_based_trimestral'),
    path('report/<int:year>/trimestral/<slug:name_slug>/', views.report_based_trimestral_detail, name='report_based_trimestral_detail'),
    path('report/<int:year>/mensual/', views.report_based_mensual, name='report_based_mensual'),
    path('report/<int:year>/mensual/<slug:name_slug>/', views.report_based_mensual_detail, name='report_based_mensual_detail'),

    path('report/<int:year>/<slug:name_cat_slug>/', views.report_based_catagenda_annual, name='report_based_catagenda_annual'),



    path('report/all/agenda/', views.print_all_report_agenda, name='print_all_report_agenda'),
    path('completed-agenda/download/csv/', views.download_Completed_Agenda_CSV, name='download_Completed_Agenda_CSV'),
    path('concluded-agenda/download/csv/', views.download_Concluded_Agenda_CSV, name='download_Concluded_Agenda_CSV'),
    path('upcoming-agenda/download/csv/', views.download_Upcoming_Agenda_CSV, name='download_Upcoming_Agenda_CSV'),

]
