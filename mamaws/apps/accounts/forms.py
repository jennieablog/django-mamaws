# apps/accounts/forms.py
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

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=_("First name"), required=True)
    last_name = forms.CharField(max_length=30, label=_("Last name"), required=True)

    def signup(self, request, user):
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
