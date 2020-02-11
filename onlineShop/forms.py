from datetime import date
from django import forms
from django.utils.timezone import now

from .models import Product
# from cartonLove_project.onlineShop.models import Cart, CartItem, Order


# form for adding the given product to the cart
class AddProductForm(forms.Form):
    
    quantity = forms.IntegerField(label="Quantity", min_value=1)
    def __init__(self, *args, **kwargs):
        self._product = kwargs.pop("product", None)
        self._to_cart = kwargs.pop("to_cart")
        super(AddProductForm, self).__init__(*args, **kwargs)


# Model form for each item in the cart used for the `CartItemFormSet`
# below which controls editing the entire cart.
class CartItemForm(forms.ModelForm):

    quantity = forms.IntegerField(label="Quantity", min_value=0)