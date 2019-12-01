from django.shortcuts import render, redirect, reverse

def view_donate(request):
    return render(request, "donate.html")

def amount_to_donate(request):
    total = int(request.POST.get('total'))
    
    donate = request.session.get('cart', {})
    if id in donate:
        donate[id] = int(donate[id]) + total
    else:
        donate[id] = donate.get(id, total)
    
    request.session['donate'] = donate
    return redirect(reverse('index'))