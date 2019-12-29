from django.shortcuts import render
from .models import Housing

def projects(request):
    return render(request, "projects.html")

def housing(request):
    housing = Housing.objects.all()
    return render(request, "housing.html", {"housing": housing})