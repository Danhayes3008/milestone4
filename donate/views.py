from django.shortcuts import render, redirect, reverse

def view_donate(request):
    return render(request, "donate.html")
