from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Homepage
    path("login/", views.login_view, name="login"), # Login
    path("dashboard/", views.dashboard, name="dashboard"), # Dashboard
]