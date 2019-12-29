from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms  import MakePaymentForm, DonationsForm
from .models import DonationsLineItem
from django.conf import settings 
from django.utils import timezone
from projects.models import Donations
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def payment(request):
    if request.method=="POST":
        donations_form = DonationsForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if donations_form.is_valid() and payment_form.is_valid():
            donation = donations_form.save(commit=False)
            donation.date = timezone.now()
            donation.save()
            
            cart = request.session.get('cart', {})
            total = 0
           
    
    return render(request, "checkout.html")