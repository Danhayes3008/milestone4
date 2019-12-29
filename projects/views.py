from django.shortcuts import render
from .models import Donations

def projects(request):
    donations = Donations.objects.all()
    return render(request, "projects.html",  {"donations": donations})