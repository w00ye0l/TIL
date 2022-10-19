from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from articles.models import Article

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("main")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.user.is_authenticated:
        return redirect("articles:index")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect(request.GET.get("next") or "articles:index")
        else:
            form = AuthenticationForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/login.html", context)


@login_required
def logout(request):
    auth_logout(request)
    messages.warning(request, "로그아웃 하였습니다.")
    return redirect("main")


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    articles = Article.objects.filter(user=user).order_by("-pk")
    context = {
        "user": user,
        "articles": articles,
    }
    return render(request, "accounts/detail.html", context)
