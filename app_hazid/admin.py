from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Survey


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("author", "swa_applied", )
    list_filter = ("swa_applied",)
