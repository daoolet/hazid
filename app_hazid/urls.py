from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("read/<int:survey_id>/", views.read_survey, name="read_survey"),
    path("create/", views.create_survey, name="create_survey"),
    path("profile/", views.profile_view, name="profile"),
    path("stats/", views.stats, name="stats"),
    path("winners/", views.winners, name="winners"),
    path("qr/", views.qr, name="qr"),

    path('profile/change_password/', views.custom_password_change, name='password_change'),
]