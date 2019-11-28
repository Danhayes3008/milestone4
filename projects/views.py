from django.shortcuts import render
from .models import Projects

def projects(request):
    donation = Projects.objects.all()
    return render(request, "projects.html", {"donation": donation})

def housing(request):
    return render(request, "housing.html")

def training(request):
    return render(request, "training.html")

def support(request):
    return render(request, "generalSupport.html")