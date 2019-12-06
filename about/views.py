from django.shortcuts import render
from .models import total_homeless, yearly_homeless

def about(request):
    return render(request, "about.html")

def Homeless(request):
    homeless = total_homeless.objects.all()
    return render(request, {"homeless": homeless})

def yearlyTotal(request):
    total = yearly_homeless.objects.all()
    return render(request, {"total": total})