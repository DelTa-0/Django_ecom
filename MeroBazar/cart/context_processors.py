from .cart import Cart 

#create context processor so cart can work in all pages

def cart(request):
    #return default data from our cart
    return{'cart':Cart(request)}