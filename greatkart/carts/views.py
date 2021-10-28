from django.shortcuts import render

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()



def cart(request):
    return render(request,'store/cart.html')