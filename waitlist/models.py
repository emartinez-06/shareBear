import random
import string
from django.db import models

class WaitlistEntry(models.Model):
    INTENT_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
        ('BOTH', 'Both'),
    ]

    CLASSIFICATION_CHOICES = [
        ('FRESHMAN', 'Freshman'),
        ('SOPHOMORE', 'Sophomore'),
        ('JUNIOR', 'Junior'),
        ('SENIOR', 'Senior'),
    ]

    email = models.EmailField(unique=True)
    intent = models.CharField(
        max_length=4, 
        choices=INTENT_CHOICES, 
        default='BOTH',
        help_text="User's primary intent on the platform."
    )
    classification = models.CharField(
        max_length=10, 
        choices=CLASSIFICATION_CHOICES, 
        blank=True, 
        null=True,
        help_text="User's academic classification."
    )
    
    # Referral System Fields
    referral_code = models.CharField(max_length=20, unique=True, blank=True)
    referred_by = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='referrals',
        help_text="The user who referred this entry."
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def referral_count(self):
        """Returns the number of users this entry has directly referred."""
        return self.referrals.count()

    def save(self, *args, **kwargs):
        # Automatically generate a referral code on creation if one isn't set
        if not self.referral_code:
            self.referral_code = self.generate_referral_code()
        super().save(*args, **kwargs)

    def generate_referral_code(self):
        # Generate a random 8-character alphanumeric code
        length = 8
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
            if not WaitlistEntry.objects.filter(referral_code=code).exists():
                return code

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Waitlist Entry"
        verbose_name_plural = "Waitlist Entries"
