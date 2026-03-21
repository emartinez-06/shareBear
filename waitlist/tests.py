from django.test import TestCase
from django.urls import reverse
from .models import WaitlistEntry

class WaitlistEntryTests(TestCase):
    def test_baylor_email_validation(self):
        """Test that only @baylor.edu emails are accepted."""
        response = self.client.post(reverse('home'), {
            'email': 'test@gmail.com',
            'intent': 'BUY',
            'year': 'FRESHMAN'
        })
        self.assertFormError(response, 'form', 'email', "Registration is currently limited to @baylor.edu email addresses.")

    def test_successful_registration(self):
        """Test that a valid registration is successful."""
        response = self.client.post(reverse('home'), {
            'email': 'test@baylor.edu',
            'intent': 'BOTH',
            'year': 'SENIOR'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(WaitlistEntry.objects.filter(email='test@baylor.edu').exists())
