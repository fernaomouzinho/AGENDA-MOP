from django.urls import path
from . import views

urlpatterns = [
    path('agenda/', views.agenda_list, name='agenda_list'),
    path('agenda/add/', views.agenda_add, name='agenda_add'),
    path('agenda/edit=?<int:pk>', views.agenda_edit, name='agenda_edit'),
    path('agenda/delete=?<int:pk>', views.agenda_delete, name='agenda_delete'),

    path('completed-agenda/', views.completedAgenda_list,
         name='completedAgenda_list'),

    path('concluded-agenda/', views.concludedAgenda_list,
         name='concludedAgenda_list'),
    path('concluded-agenda/<slug:title_slug>',
         views.concludedAgenda_list_detail, name='concludedAgenda_list_detail'),
    path('concluded-agenda/comment/add/<int:pk>',
         views.commentCoAgenda_add, name='commentCoAgenda_add'),



    path('canceled-agenda/', views.canceledAgenda_list,
         name='canceledAgenda_list'),
    path('canceled-agenda/<slug:title_slug>',
         views.canceledAgenda_list_detail, name='canceledAgenda_list_detail'),
    path('canceled-agenda/comment/add/<int:pk>',
         views.commentCaAgenda_add, name='commentCaAgenda_add'),

    path('running-agenda/', views.runningAgenda_list, name='runningAgenda_list'),
    path('running-agenda/<slug:title_slug>',
         views.runningAgenda_list_detail, name='runningAgenda_list_detail'),
    path('running-agenda/comment/add/<int:pk>',
         views.commentRuAgenda_add, name='commentRuAgenda_add'),

    path('upcoming-agenda/', views.upcomingAgenda_list,
         name='upcomingAgenda_list'),
    path('upcoming-agenda/<slug:title_slug>',
         views.upcomingAgenda_list_detail, name='upcomingAgenda_list_detail'),
    path('upcoming-agenda/edit:$<str:pk>',
         views.upcomingAgenda_edit, name='upcomingAgenda_edit'),
    path('upcoming-agenda/delete:?<int:pk>',
         views.upcomingAgenda_delete, name='upcomingAgenda_delete'),
    path('upcoming-agenda/cancel:?<int:pk>',
         views.upcomingAgenda_cancel, name='upcomingAgenda_cancel'),
    path('upcoming-agenda-read/', views.upcomingAgenda_read,
         name='upcomingAgenda_read'),
    path('postpone-agenda/?<int:pk>',
         views.postponeAgenda_list, name='postponeAgenda_list'),

    path('request-agenda/', views.requestedagenda_list,
         name='requestedagenda_list'),
    path('request-agenda/add/', views.requestedagenda_add,
         name='requestedagenda_add'),

    path('request-agenda/waitting/list/', views.waitting_requestedagenda_list,
         name='waitting_requestedagenda_list'),





    path('informative-note/', views.informative_list, name='informative_list'),
    path('informative-note/add/', views.informative_add, name='informative_add'),
    path('informative-note/edit=?<int:pk>',
         views.informative_edit, name='informative_edit'),
    path('informative-note/delete=?<int:pk>',
         views.informative_delete, name='informative_delete'),
    path('completed-informative/', views.completedInformative_list,
         name='completedInformative_list'),

    path('executed-informative/', views.executedInformative_list,
         name='executedInformative_list'),
    path('executed-informative/<slug:title_slug>',
         views.executedInformative_list_detail, name='executedInformative_list_detail'),
    path('executed-informative/change/<int:pk>',
         views.executeInformative_change, name='executeInformative_change'),
    path('executed-informative/comment/add/<int:pk>',
         views.commentExInformative_add, name='commentExInformative_add'),
    path('executed-informative/comment/edit/<int:pk>',
         views.commentExInformative_edit, name='commentExInformative_edit'),




    path('unxecuted-informative/', views.unexecutedInformative_list,
         name='unexecutedInformative_list'),




]
