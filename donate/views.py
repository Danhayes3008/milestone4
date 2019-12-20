from django.shortcuts import render, redirect, reverse
from projects.models import Housing

# Create your views here.
def view_donate(request):
    """A View that renders the cart contents page"""
    return render(request, "donate.html")


def amount_to_donate(request, id):
    """Add a quantity of the specified product to the cart"""
    amount = int(request.POST.get('amount'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + amount      
    else:
        cart[id] = cart.get(id, amount) 

    request.session['cart'] = cart
    return redirect(reverse('donation'))


def adjust_donation(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    print(request.POST)
    amount = int(request.POST.get('amount'))
    cart = request.session.get('cart', {})

    if amount > 0:
        cart[id] = amount
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_donate'))