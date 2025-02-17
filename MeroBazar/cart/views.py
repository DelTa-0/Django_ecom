from django.shortcuts import render,redirect,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    return render(request,'cart_summary.html',{})

def cart_add(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        #get stuff
        product_id=int(request.POST.get('product_id'))
        if not product_id:
            return JsonResponse({"error": "Missing product_id"}, status=400)
        #lookup product
        product=get_object_or_404(Product,id=product_id)
        #save to session
        cart.add(product=product)
        #get cart quantity
        cart_quantity=cart.__len__()
        #return response
        # response=JsonResponse({'Product Name: ':product.name})
        response=JsonResponse({'qty: ':cart_quantity})
        return response


def cart_delete(request):
    pass

def cart_update(request):
    pass