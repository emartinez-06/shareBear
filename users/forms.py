from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError
import re


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'intent', 'classification')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.lower().endswith('@baylor.edu'):
            raise ValidationError(
                "Registration is currently limited to @baylor.edu email addresses.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data.get('email')

        # Extract the part before @baylor.edu
        local_part = email.split('@')[0]

        # Baylor emails format: FirstName_LastName(#)
        # We replace underscores with spaces to make a nice display name
        display_name = local_part.replace('_', ' ')

        # Ensure title case for names (e.g., "erick martinez4" -> "Erick Martinez4")
        # We split, capitalize purely alphabetic parts, and rejoin to preserve numbers
        parts = display_name.split(' ')
        capitalized_parts = []
        for part in parts:
            # Separate the alphabetic name from the potential trailing number
            match = re.match(r'([A-Za-z]+)(\d*)', part)
            if match:
                name_str, number_str = match.groups()
                capitalized_parts.append(name_str.capitalize() + number_str)
            else:
                capitalized_parts.append(part.capitalize())

        user.username = ' '.join(capitalized_parts)

        if commit:
            user.save()
        return user
