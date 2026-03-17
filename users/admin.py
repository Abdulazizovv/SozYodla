from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "date_joined", "last_login", "is_superuser", "is_staff", "is_active"]
    list_display_links = ["email"]