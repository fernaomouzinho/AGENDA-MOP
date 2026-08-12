from django.urls import path, re_path
from agendaapps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),


]