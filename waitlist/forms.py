from django import forms
from .models import WaitlistEntry
from django.core.exceptions import ValidationError

class WaitlistEntryForm(forms.ModelForm):
    class Meta:
        model = WaitlistEntry
        fields = ('email', 'first_name', 'last_name', 'intent', 'year')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            return email
        email = email.lower()
        if not email.endswith('@baylor.edu'):
            raise ValidationError(
                "Registration is currently limited to @baylor.edu email addresses.")
        if WaitlistEntry.objects.filter(email=email).exists():
             raise ValidationError("This email is already on the waitlist.")
        return email
