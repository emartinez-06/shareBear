from django import forms
from .models import WaitlistEntry
from django.core.exceptions import ValidationError

class WaitlistEntryForm(forms.ModelForm):
    class Meta:
        model = WaitlistEntry
        fields = ('email', 'intent', 'classification', 'referred_by')
        widgets = {
            'referred_by': forms.HiddenInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.lower().endswith('@baylor.edu'):
            raise ValidationError(
                "Registration is currently limited to @baylor.edu email addresses.")
        if WaitlistEntry.objects.filter(email=email).exists():
             raise ValidationError("This email is already on the waitlist.")
        return email
