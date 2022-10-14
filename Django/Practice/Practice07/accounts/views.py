from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    users = get_user_model().objects.all()

    context = {
        "users": users,
    }

    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm()
        if form.is_valid():
            form.save()
            return redirect("accounts/index")
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/signup.html", context)


def login(request):
    if request.user.is_authenticated:
        return redirect("accounts:index")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect(request.GET.get("next") or "accounts:index")
        else:
            form = AuthenticationForm()

        context = {
            "form": form,
        }

        return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)

    return redirect("index")
