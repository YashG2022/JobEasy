# JobEasy/admin.py
from django.contrib import admin
from .models import UserQuery

# Register the UserQuery model to show in admin console
@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    list_display = ('user', 'query', 'created_at')  # Columns to display in the admin panel
    search_fields = ('user__username', 'query')  # Add search functionality
    list_filter = ('created_at',)  # Add filter by creation date
