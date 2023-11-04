from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count
from django.views import View
from django.utils.decorators import method_decorator

from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib import messages


from .models import Survey
from .forms import SurveyForm

from app_users.models import AllowedUser
from app_users.forms import LoginUserForm, RegisterUserForm, ChangePasswordForm, AllowedUserForm


def custom_register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data["email"]
            
            # if user exist in allowed list
            if AllowedUser.objects.filter(email = user_email).exists():
                form.save()
                user = form.save()

                if "@admin" in user.email:
                    group = Group.objects.get(name="admin")
                else:
                    group = Group.objects.get(name="default")
                group.user_set.add(user)

                return redirect(reverse("index"))
            else:
                return render(
                    request,
                    "registration/register.html",
                    {
                        "form": form,
                        "error_message": "You are not allowed to register."
                    }
                )
    else:
        form = RegisterUserForm()
    return render(request, "registration/register.html", {"form": form})


def custom_login(request):
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("app_hazid:index")
    else:
        form = LoginUserForm()
    return render(request, "registration/login.html", {"form": form})


@login_required(login_url="/login/")
def custom_password_change(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            # messages.success(request, "Password changed successfully")
            return redirect("about_me")
    else:
        form = ChangePasswordForm(request.user)
    return render(request, "registration/password_change/password_change_form.html", {"form": form})


@login_required(login_url="/login")
def index(request):
    surveys = Survey.objects.all()
    context = {
        "surveys": surveys[::-1],
    }
    return render(request, "app_hazid/index.html", context)


@login_required(login_url="/login")
def create_survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.author = request.user
            survey.save()
            return redirect(reverse("read_survey", args=(survey.id,)))
    else:
        form = SurveyForm()
    return render(request, "app_hazid/create_survey.html", {"form": form})


def read_survey(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    context = {
        "survey": survey,
    }
    return render(request, "app_hazid/detail.html", context)


@login_required(login_url="/login/")
def profile_view(request):
    if request.method == "POST":
        form = AllowedUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("profile"))
    else:
        form = AllowedUserForm()

    current_user = request.user
    surveys = Survey.objects.filter(author_id=current_user.id)

    context = {
        "current_user": current_user,
        "current_user_id": current_user.id,
        "surveys": surveys,
        "form": form,
    }

    return render(request, "app_hazid/profile.html", context)


def stats(request):
    team_size = AllowedUser.objects.count()
    card_submitted = Survey.objects.count()
    individuals = Survey.objects.values("author_id").annotate(count=Count("author_id"))
    observed_counts = Survey.objects.values("i_observed").annotate(count=Count("i_observed"))

    target_achieved = round(card_submitted * 100 / team_size)
    individuals_percentage = round(individuals.count() * 100 / team_size)

    context = {
        "observed_counts": observed_counts,
        "card_submitted": card_submitted,
        "individuals": individuals,
        "team_size": team_size,
        "target_achieved": target_achieved,
        "individuals_percentage": individuals_percentage,
    }
    return render(request, "app_hazid/stats.html", context)


def winners(request):
    context = {

    }
    return render(request, "app_hazid/winners.html", context)


def qr(request): 
    context = {

    }
    return render(request, "app_hazid/qr.html", context)



