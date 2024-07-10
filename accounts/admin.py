from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Customer

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'phone_number', 'address', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone_number', 'address', 'profile_image')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone_number', 'address', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Customer, UserAdmin)
