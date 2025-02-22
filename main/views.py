from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, "main/home.html")


def login_view(request):
    if request.user.is_authenticated:  # 🔹 If already logged in, go to dashboard
        return redirect("dashboard")

    login_form = AuthenticationForm(request, data=request.POST or None)
    register_form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        if "login_submit" in request.POST:  # 🔹 User is trying to log in
            if login_form.is_valid():
                user = login_form.get_user()
                if not user:
                    messages.error(
                        request,
                        "Login attempt unsuccessful. Please re-enter your username and password.",
                    )
                login(request, user)
                return redirect("dashboard")  # ✅ Redirect to dashboard after login

        elif "register_submit" in request.POST:
            if register_form.is_valid():
                register_form.save()
                messages.success(
                    request, "Your account has been created! Please log in."
                )
                return redirect("login")  # ✅ Redirect back to login page

    return render(
        request,
        "main/login.html",
        {
            "login_form": login_form,
            "register_form": register_form,
        },
    )


def dashboard(request):
    return render(request, "main/dashboard.html")
