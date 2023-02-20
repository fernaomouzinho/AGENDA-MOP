from django.urls import path
from . import views

urlpatterns = [
    path('agenda/', views.agenda_list, name='agenda_list'),
    path('agenda/add/', views.agenda_add, name='agenda_add'),
    path('agenda/edit=?<int:pk>', views.agenda_edit, name='agenda_edit'),
    path('agenda/delete=?<int:pk>', views.agenda_delete, name='agenda_delete'),
    path('completed-agenda/', views.completed_view, name='completed_view'),
    path('completed-agenda/<slug:title_slug>', views.completed_view_detail, name='completed_view_detail'),
    path('canceled-agenda/', views.canceled_view, name='canceled_view'),
    path('canceled-agenda/<slug:title_slug>', views.canceled_view_detail, name='canceled_view_detail'),
    path('running-agenda/', views.running_view, name='running_view'),
    path('running-agenda/<slug:title_slug>', views.running_view_detail, name='running_view_detail'),
    path('upcoming-agenda/', views.upcoming_view, name='upcoming_view'),
    path('upcoming-agenda/<slug:title_slug>', views.upcoming_view_detail, name='upcoming_view_detail'),
    path('upcoming-agenda/edit:$<str:pk>', views.upcoming_edit, name='upcoming_edit'),
    path('upcoming-agenda/delete:?<int:pk>', views.upcoming_delete, name='upcoming_delete'),
    path('upcoming-agenda/cancel:?<int:pk>', views.upcoming_cancel, name='upcoming_cancel'),
]