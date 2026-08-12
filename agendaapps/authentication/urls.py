from django.urls import path
from .views import login_view, register_user, change_password,custom_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', login_view, name="login"),
    # path('register/', register_user, name="register"),
    # path("logout/", custom_logout, name="logout"),
    # path('password/', change_password, name='change_password'),
]
