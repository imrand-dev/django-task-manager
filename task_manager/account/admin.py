from django.contrib import admin

from account.models import User 
from account.forms import UserCreationForm

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["first_name", "last_name", "email"]
    search_fields = ("email",)
    ordering = ("email",)
    list_filter = ("email", "is_staff", "is_active",)
    form = UserCreationForm

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Other",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "avatar",
                )
            },
        ),
        (
            "User Permission",
            {
                "fields": (
                    "is_superuser",
                    "is_staff",
                    "is_verified",
                    "is_active",
                )
            },
        ),
        ("Groups and Permissions", {"fields": ("groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            'classes': ("wide",),
            'fields': ("first_name", "last_name", "email", "password1", "password2", "avatar"),
        }),
    )
