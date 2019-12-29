from django.shortcuts import get_object_or_404
from projects.models import Donations

def housing_cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    project_count = 0
    for id, amount in cart.items():
        donations = get_object_or_404(Donations, pk=id)
        total += amount * donations.donation
        project_count += amount
        cart_items.append({'id':id, 'amount':amount, 'donations':donations})
        
    return {'cart_items': cart_items, 'total':total, 'project_count':project_count}