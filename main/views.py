from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, "main/home.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    login_form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        # Process login submission
        if login_form.is_valid():
            user = login_form.get_user()
            if user:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(
                    request,
                    "Login attempt unsuccessful. Please re-enter your username and password.",
                )
    return render(request, "accounts/login.html", {"login_form": login_form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    register_form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        # Process registration submission
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Your account has been created! Please log in.")
            return redirect("login")
    return render(request, "accounts/register.html", {"register_form": register_form})


def dashboard(request):
    return render(request, "main/dashboard.html")

def grocery_search(request):
    return render(request, 'main/grocerysearch.html')
