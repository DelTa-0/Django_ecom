from django.shortcuts import render,redirect,get_object_or_404
from .cart import Cart
from store.models import Product
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_prods
    quantities=cart.get_quants
    return render(request,'cart_summary.html',{
        'cart_products':cart_products,
        'quantities':quantities
    })

def cart_add(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        #get stuff
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        # product_qty = request.POST.get('product_qty', '0')  # Default to '0' if empty
        # product_qty = int(product_qty) if product_qty.isdigit() else 0  # Convert safely

        if not product_id:
            return JsonResponse({"error": "Missing product_id"}, status=400)
        #lookup product
        product=get_object_or_404(Product,id=product_id)
        #save to session
        cart.add(product=product,quantity=product_qty)
        #get cart quantity
        cart_quantity=cart.__len__()
        #return response
        # response=JsonResponse({'Product Name: ':product.name})
        response=JsonResponse({'qty':cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response


def cart_delete(request):
    pass

def cart_update(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        #get stuff
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        cart.update(product=product_id,quantity=product_qty)

        response=JsonResponse({'qty':product_qty})
        return response
        
    