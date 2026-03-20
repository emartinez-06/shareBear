from django.contrib import admin
from .models import WaitlistEntry

@admin.register(WaitlistEntry)
class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'intent', 'year', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('created_at',)
