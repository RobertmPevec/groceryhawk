from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Homepage
    path("login/", views.login_view, name="login"),  # Login
    path("create-account/", views.register_view, name="register"),  # Register
    path("dashboard/", views.dashboard, name="dashboard"),  # Dashboard
    path('grocery-search/', views.grocery_search, name='grocery_search'), # Grocery Search
]
