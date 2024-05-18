from django.shortcuts import render
from .models import Profile

def view_page(request):
    profile = Profile.objects.first()
    return render(request, 'profile.html', {'profile': profile})
