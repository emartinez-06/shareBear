import random
import string
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    # Use the custom manager
    objects = CustomUserManager()

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
        help_text="User's primary intent on the platform. Used for analytics."
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
        help_text="The user who referred this user."
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def referral_count(self):
        """Returns the number of users this user has directly referred."""
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
            if not User.objects.filter(referral_code=code).exists():
                return code

    def __str__(self):
        return self.username
