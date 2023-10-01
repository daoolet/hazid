from django.contrib import admin

from .models import CustomUser, AllowedUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email",)
    filter_horizontal = ("groups",)


class AllowedUserAdmin(admin.ModelAdmin):
    list_display = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AllowedUser, AllowedUserAdmin)
