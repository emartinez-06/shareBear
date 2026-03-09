from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'intent', 'classification', 'referral_code', 'referral_count', 'is_staff']
    
    # Fields to show when editing an existing user
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Information', {'fields': ('intent', 'classification', 'referral_code', 'referred_by')}),
    )
    
    # Fields to show when adding a new user manually in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Information', {'fields': ('email', 'intent', 'classification')}),
    )

    search_fields = ('email', 'username', 'referral_code')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
