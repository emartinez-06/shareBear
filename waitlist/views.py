from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import WaitlistEntryForm

def home(request):
    if request.method == 'POST':
        form = WaitlistEntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for joining the waitlist! We'll be in touch soon.")
            return redirect('home')
    else:
        form = WaitlistEntryForm()

    return render(request, 'home.html', {'form': form})
