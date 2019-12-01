from django.shortcuts import render
from .models import Housing, Training, Support

def projects(request):
    return render(request, "projects.html")

def housing(request):
    housing = Housing.objects.all()
    return render(request, "housing.html", {"housing": housing})

def training(request):
    training = Training.objects.all()
    return render(request, "training.html", {"training": training})

def support(request):
    support = Support.objects.all()
    return render(request, "generalSupport.html", {"support": support})