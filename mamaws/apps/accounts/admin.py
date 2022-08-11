# accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm, AccountChangeForm
from .models import Account

class AccountAdmin(UserAdmin):
	fieldsets = (
		(None, {
			'fields': ('username', 'password')
		}),
		('Profile', {
			'fields': ('email','first_name', 'last_name','active_purchase_id')
		}),
		('Activity Log', {
			'fields': ('created_at', 'updated_at', 'last_login',),
			'classes': ('collapse',),
		}),
		('Permissions', {
			'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
			'classes': ('collapse',),
		}),
	)

	add_form = AccountCreationForm
	form = AccountChangeForm
	model = Account
	list_display = ['email', 'username',]
	readonly_fields = ['created_at', 'updated_at', 'last_login']

admin.site.register(Account, AccountAdmin)