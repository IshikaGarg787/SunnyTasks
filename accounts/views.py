from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def register(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        confirm_password = request.POST.get(
            "confirm_password"
        )

        if password == confirm_password:

            User.objects.create_user(
                username=username,
                password=password
            )

            return redirect("login")

    return render(
        request,
        "accounts/register.html"
    )

def user_login(request):

    error = ""

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        else:

            error = "Invalid username or password"

    return render(
        request,
        "accounts/login.html",
        {"error": error}
    )

def user_logout(request):

    logout(request)

    return redirect("login")