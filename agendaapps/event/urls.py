from django.urls import path
from . import views

urlpatterns = [
    path('agenda/type/',views.typeagenda_list, name='typeagenda_list'),
    path('agenda/type/edit/<uuid:uuid>/',views.typeagenda_edit,name='typeagenda_edit'),
    path('agenda/type/delete/<uuid:uuid>/',views.typeagenda_delete,name='typeagenda_delete'),
    path('category-agenda/', views.categoryagenda_list,name='categoryagenda_list'),
    path('category-agenda/<uuid:uuid>/edit/',views.categoryagenda_edit, name='categoryagenda_edit'),
    path('category-agenda/<uuid:uuid>/delete/',views.categoryagenda_delete, name='categoryagenda_delete'),
    path('agenda/', views.agenda_list, name='agenda_list'),
    path('agenda/add/', views.agenda_add, name='agenda_add'),
    path('agenda/<uuid:uuid>/edit/', views.agenda_edit, name='agenda_edit'),
    path('agenda/<uuid:uuid>/delete/', views.agenda_delete, name='agenda_delete'),
    
    path('agenda/to/', views.agendato_list, name='agendato_list'),
    path('agenda/to/<uuid:uuid>/edit/',views.agendato_edit,name='agendato_edit'),
    path('agenda/to/<uuid:uuid>/delete/',views.agendato_delete,name='agendato_delete'),
    
    path('agenda/delegation/', views.agenda_delegation_list, name='agenda_delegation_list'),
    path('agenda/delegation/<uuid:uuid>/',views.agenda_delegation_detail,name='agenda_delegation_detail'),
    
    
    path("notification/",views.notification_list,name="notification_list"),
    path("notification/live/",views.notification_live,name="notification_live"),
    path("notification/<uuid:uuid>/open/",views.notification_open,name="notification_open"),
    path("notification/mark-all-read/",views.notification_mark_all_read,name="notification_mark_all_read"),
   
   
    path('completed-agenda/', views.completedAgenda_list,name='completedAgenda_list'),
    path('concluded-agenda/', views.concludedAgenda_list,  name='concludedAgenda_list'),
    path('concluded-agenda/<slug:title_slug>', views.concludedAgenda_list_detail, name='concludedAgenda_list_detail'),
    path('concluded-agenda/comment/add/<int:pk>', views.commentCoAgenda_add, name='commentCoAgenda_add'),



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
    path('running-agenda/change/time/<int:pk>',
         views.runningagenda_change, name='runningagenda_change'),
    path('running-agenda/stop/time/<int:pk>',
         views.runningagenda_stop, name='runningagenda_stop'),


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
    path('request-agenda/edit:?<int:pk>', views.requestedagenda_edit,
         name='requestedagenda_edit'),
    path('request-agenda/delete:?<int:pk>', views.requestedagenda_delete,
         name='requestedagenda_delete'),
    path('request-agenda/waitting/<int:pk>', views.waitting_requestedagenda_list,
         name='waitting_requestedagenda_list'),
    path('request-agenda/approve/<int:pk>', views.requestedagenda_approve,
         name='requestedagenda_approve'),
    path('request-agenda/read/', views.requestedagenda_read,
         name='requestedagenda_read'),

    path('request-agenda/waitting/uga/', views.waitting_requestedagendauga_list,
         name='waitting_requestedagendauga_list'),
    path('request-agenda/waitting/uap/', views.waitting_requestedagendauap_list,
         name='waitting_requestedagendauap_list'),
    path('request-agenda/waitting/ucvq/', views.waitting_requestedagendaucvq_list,
         name='waitting_requestedagendaucvq_list'),
    path('request-agenda/waitting/uedc/', views.waitting_requestedagendauedc_list,
         name='waitting_requestedagendauedc_list'),

     path('request-agenda/approve/uga/', views.approved_requestedagendauga_list,
         name='approved_requestedagendauga_list'),
    path('request-agenda/approve/uap/', views.approved_requestedagendauap_list,
         name='approved_requestedagendauap_list'),
    path('request-agenda/approve/ucvq/', views.approved_requestedagendaucvq_list,
         name='approved_requestedagendaucvq_list'),
    path('request-agenda/approve/uedc/', views.approved_requestedagendauedc_list,
         name='approved_requestedagendauedc_list'),

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
    
    path('notification/read/',views.agenda_notification_read,name='agenda_notification_read'),
    
    path("recipient/",views.recipient_list,name="recipient_list"),
    path("recipient/add/",views.recipient_add,name="recipient_add"),
    path("recipient/<uuid:uuid>/edit/",views.recipient_edit,name="recipient_edit"),
    path("recipient/<uuid:uuid>/delete/",views.recipient_delete,name="recipient_delete"),
    
]
