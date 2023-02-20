from django.urls import path
from . import views

urlpatterns = [
    path('institution/', views.institution_list, name='institution_list'),
    path('institution/add/', views.institution_add, name='institution_add'),
    path('institution/edit=?<int:pk>', views.institution_edit, name='institution_edit'),
    path('institution/delete=?<int:pk>', views.institution_delete, name='institution_delete'),
    path('attendant/', views.attendence_list, name='attendence_list'),
    path('attendant/add/', views.attendence_add, name='attendence_add'),
    path('attendant/edit=?<int:pk>', views.attendence_edit, name='attendence_edit'),
    path('attendant/delete=?<int:pk>', views.attendence_delete, name='attendence_delete'),
    
]