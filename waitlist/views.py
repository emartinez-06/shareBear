from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import WaitlistEntryForm

def home(request):
    if request.method == 'POST':
        form = WaitlistEntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for joining the waitlist! We'll be in touch soon.")
            return redirect('/#waitlist')
    else:
        form = WaitlistEntryForm()

    return render(request, 'home.html', {'form': form})

def process(request):
    return render(request, 'process.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')
