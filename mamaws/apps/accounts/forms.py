#forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import Account

class AccountCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = (
					'username',
					'email',
					# other fields
				)

class AccountChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = (
						'first_name',
						'last_name',
						# other fields
				)