from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Product
from .models import Cart
from .models import CartItem
from .models import SelectedProduct
from .forms import AddProductForm

def base(request):
    template = loader.get_template('onlineShop/base.html')
    return render(request, 'onlineShop/base.html')


def home(request):
    template = loader.get_template('onlineShop/home.html')
    return render(request, 'onlineShop/home.html',)


# Display products + handle add item to cart
def shopping(request,  
            #form_class = AddProductForm
            ):
    template = loader.get_template('onlineShop/shopping.html')
    
    products = Product.objects.all()
    to_cart = (request.method == "POST")
    initial_data = {}
    # selectedProducts = SelectedProduct.objects.all()

    context = { 'products': products, 
                # 'selectedProducts': selectedProducts
                # "add_product_form": add_product_form
                #"images": products.images.all(),
    }
    return HttpResponse(template.render(context, request)) 

def cart(request):
    template = loader.get_template('onlineShop/cart.html')
    
    cartItem = CartItem.objects.all()
    
# Display cart and handle remove items from cart
# https://github.com/stephenmcd/cartridge/blob/master/cartridge/shop/views.py
# def cart(request, template="onlineShop/cart.html") :
