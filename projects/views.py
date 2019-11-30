from django.shortcuts import render
from .models import Projects

def projects(request):
    return render(request, "projects.html")

def housing(request):
    donation = Projects.objects.all()
    return render(request, "housing.html", {"donation": donation})

def training(request):
    return render(request, "training.html")

def support(request):
    return render(request, "generalSupport.html")