from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'lead_type', 'name', 'phone', 'email', 'status', 'language')
    list_filter = ('status', 'lead_type', 'language', 'created_at')
    search_fields = ('name', 'phone', 'email', 'message')
    readonly_fields = ('created_at', 'updated_at', 'source_path', 'user_agent', 'ip_address')
