from django.contrib import admin
from .models import WaitlistEntry

@admin.register(WaitlistEntry)
class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ('email', 'intent', 'classification', 'referral_code', 'referral_count', 'created_at')
    search_fields = ('email', 'referral_code')
    list_filter = ('intent', 'classification')
    readonly_fields = ('referral_code', 'referral_count', 'created_at')
