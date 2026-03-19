from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import WaitlistEntryForm
from .models import WaitlistEntry

def home(request):
    # Referral logic: Check if a 'ref' code is in the URL
    referral_code = request.GET.get('ref')
    referred_by = None
    if referral_code:
        try:
            referred_by = WaitlistEntry.objects.get(referral_code=referral_code)
        except WaitlistEntry.DoesNotExist:
            pass

    if request.method == 'POST':
        form = WaitlistEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            if referred_by:
                entry.referred_by = referred_by
            entry.save()
            messages.success(request, f"Thanks for joining! Your referral code is {entry.referral_code}")
            # Optionally store the referral code in session or just show it
            return render(request, 'home.html', {'entry': entry, 'form': WaitlistEntryForm()})
    else:
        # Pre-fill referred_by if found
        initial_data = {}
        if referred_by:
            initial_data['referred_by'] = referred_by
        form = WaitlistEntryForm(initial=initial_data)

    return render(request, 'home.html', {'form': form})
