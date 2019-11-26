from django.shortcuts import render
from .models import Projects

def projects(request):
    donation = Projects.objects.all()
    return render(request, "projects.html", {"donation": donation})