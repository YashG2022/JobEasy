# chatbot/admin.py
from django.contrib import admin
from .models import Chat

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'created_at')  # Columns to display
    search_fields = ('user__username', 'question')  # Enable search on username and question
    list_filter = ('created_at',)  # Add filter by creation date
    ordering = ('-created_at',)  # Order by creation date, descending
