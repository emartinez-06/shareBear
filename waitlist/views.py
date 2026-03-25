import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import WaitlistEntryForm

logger = logging.getLogger(__name__)


def _send_waitlist_welcome_email(entry):
    """
    Send confirmation/welcome email after waitlist signup.
    Skips if Gmail credentials are not configured (set EMAIL_HOST_USER + EMAIL_HOST_PASSWORD).
    Edit templates under templates/waitlist/emails/ for copy and styling.
    """
    if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
        return

    context = {
        'entry': entry,
        'first_name': (entry.first_name or '').strip(),
    }
    subject = render_to_string(
        'waitlist/emails/welcome_waitlist_subject.txt', context
    ).strip()
    text_body = render_to_string('waitlist/emails/welcome_waitlist.txt', context)
    html_body = render_to_string('waitlist/emails/welcome_waitlist.html', context)

    try:
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[entry.email],
        )
        msg.attach_alternative(html_body, 'text/html')
        msg.send(fail_silently=False)
    except Exception:
        logger.exception(
            'Failed to send waitlist welcome email to %s', entry.email
        )


def home(request):
    if request.method == 'POST':
        form = WaitlistEntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            _send_waitlist_welcome_email(entry)
            messages.success(request, "Thanks for joining the waitlist! We'll be in touch soon.")
            return redirect('home')
    else:
        form = WaitlistEntryForm()

    return render(request, 'home.html', {'form': form})

def process(request):
    return render(request, 'process.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')
