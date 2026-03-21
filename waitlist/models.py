from django.db import models

class WaitlistEntry(models.Model):
    INTENT_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
        ('BOTH', 'Both'),
    ]

    YEAR_CHOICES = [
        ('FRESHMAN', 'Freshman'),
        ('SOPHOMORE', 'Sophomore'),
        ('JUNIOR', 'Junior'),
        ('SENIOR', 'Senior'),
        ('GRADUATE', 'Graduate'),
        ('OTHER', 'Other'),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    intent = models.CharField(
        max_length=10, 
        choices=INTENT_CHOICES, 
        default='BOTH',
    )
    year = models.CharField(
        max_length=10, 
        choices=YEAR_CHOICES, 
        blank=True, 
        null=True,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Waitlist Entry"
        verbose_name_plural = "Waitlist Entries"
