from django.shortcuts import get_object_or_404
from projects.models import Housing, Training, Support

def housing_cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    project_count = 0
    for id, amount in cart.items():
        housing = get_object_or_404(Housing, pk=id)
        total += amount * housing.donation
        project_count += amount
        cart_items.append({'id':id, 'amount':amount, 'housing':housing})
        
    return {'cart_items': cart_items, 'total':total, 'project_count':project_count}

def training_cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    project_count = 0
    for id, amount in cart.items():
        training = get_object_or_404(Training, pk=id)
        total += amount * training.donation
        project_count += amount
        cart_items.append({'id':id, 'amount':amount, 'training':training})
        
    return {'cart_items': cart_items, 'total':total, 'project_count':project_count}