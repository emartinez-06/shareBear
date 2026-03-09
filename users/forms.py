from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'intent', 'classification')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.lower().endswith('@baylor.edu'):
            raise ValidationError("Registration is currently limited to @baylor.edu email addresses.")
        return email
