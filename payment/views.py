from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms  import MakePaymentForm, DonationsForm
from .models import DonationsLineItem
from django.conf import settings 
from django.utils import timezone
from projects.models import Product
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def payment(request):
    return render(request, 'payment.html')    