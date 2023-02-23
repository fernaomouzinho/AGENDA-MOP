from django.urls import path
from . import views

urlpatterns = [
    path('agenda/', views.agenda_list, name='agenda_list'),
    path('agenda/add/', views.agenda_add, name='agenda_add'),
    path('agenda/edit=?<int:pk>', views.agenda_edit, name='agenda_edit'),
    path('agenda/delete=?<int:pk>', views.agenda_delete, name='agenda_delete'),

    path('completed-agenda/', views.completedAgenda_list, name='completedAgenda_list'),
    
    path('concluded-agenda/', views.concludedAgenda_list, name='concludedAgenda_list'),
    path('concluded-agenda/<slug:title_slug>', views.concludedAgenda_list_detail, name='concludedAgenda_list_detail'),
    path('concluded-agenda/comment/add/<int:pk>', views.commentCoAgenda_add, name='commentCoAgenda_add'),
   
    
    
    path('canceled-agenda/', views.canceledAgenda_list, name='canceledAgenda_list'),
    path('canceled-agenda/<slug:title_slug>', views.canceledAgenda_list_detail, name='canceledAgenda_list_detail'),
    path('canceled-agenda/comment/add/<int:pk>', views.commentCaAgenda_add, name='commentCaAgenda_add'),
   
    path('running-agenda/', views.runningAgenda_list, name='runningAgenda_list'),
    path('running-agenda/<slug:title_slug>', views.runningAgenda_list_detail, name='runningAgenda_list_detail'), 
    path('running-agenda/comment/add/<int:pk>', views.commentRuAgenda_add, name='commentRuAgenda_add'),
    
    path('upcoming-agenda/', views.upcomingAgenda_list, name='upcomingAgenda_list'),
    path('upcoming-agenda/<slug:title_slug>', views.upcomingAgenda_list_detail, name='upcomingAgenda_list_detail'),
    path('upcoming-agenda/edit:$<str:pk>', views.upcomingAgenda_edit, name='upcomingAgenda_edit'),
    path('upcoming-agenda/delete:?<int:pk>', views.upcomingAgenda_delete, name='upcomingAgenda_delete'),
    path('upcoming-agenda/cancel:?<int:pk>', views.upcomingAgenda_cancel, name='upcomingAgenda_cancel'),
    path('upcoming-agenda-read/', views.upcomingAgenda_read, name='upcomingAgenda_read'),
    path('postpone-agenda/?<int:pk>', views.postponeAgenda_list, name='postponeAgenda_list'),
    #path('comment-agenda/add/<int:pk>', views.commentAgenda_add, name='commentAgenda_add'),
    

    path('informative-note/', views.informative_list, name='informative_list'),
    path('informative-note/add/', views.informative_add, name='informative_add'),
    path('informative-note/edit=?<int:pk>', views.informative_edit, name='informative_edit'),
    path('informative-note/delete=?<int:pk>', views.informative_delete, name='informative_delete'),  

    path('comment-informative-note/add/<int:pk>', views.commentinformative_add, name='commentinformative_add'),


    path('concluded-informative/', views.concludedInformative_list, name='concludedInformative_list'),
    path('concluded-informative/<slug:title_slug>', views.concludedInformative_list_detail, name='concludedInformative_list_detail'),
    path('unxecuted-informative/', views.unexecutedInformative_list, name='unexecutedInformative_list'),




]