from django.db import models
from django.db.models import CharField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import datetime
from decimal import Decimal
from functools import reduce

from onlineShop import fields


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    adress_line1 = models.CharField(max_length=30)
    adress_line2 = models.CharField(max_length=30)
    zip_code = models.IntegerField(default=0)
    country = models.CharField(max_length=50)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='static/images/')
    price = models.IntegerField(default=0)
    restock_date = models.DateTimeField('date restocked')
    restock_amount = models.IntegerField(default=40)
    left_in_stock = models.IntegerField(default=40)
    def is_available(self):
        return self.left_in_stock > 0
    
    dimensions = models.CharField(max_length=20)
    weight = models.IntegerField(default=0)
    
    class PackagingType(models.TextChoices):
        FOLDING_CARTON = 'FC', _('Folding carton')
        RIGID_BOX  = 'RB', _('Rigid box')
        SHOULDER_BOX = 'SB', _('Shoulder box')
        COLLAPSIBLE_BOX = 'CB', _('Collapsible box')
        CORRUGATED_CARDBOARD_BOX = 'CCB', _('Corrugated cardboard box')

    packaging_type = models.CharField( max_length=3, choices = PackagingType.choices, default = PackagingType.FOLDING_CARTON)
        

CART_ID = 'CART-ID'

class Cart(models.Model):
    cart_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    
    def __init__(self, request):
        cart_id = request.get(CART_ID)
        if cart_id : 
            try:
                cart = models.Cart.objects.get(id=cart_id, checked_out=False)
            except models.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart
        
    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item
    
    def new(self, request):
        cart = models.Cart(creation_date = datetime.now())
        cart.save()
    #  request.session[CART_ID] = cart.id
        return cart
        
    # def add(self, product, unit_price, quantity=1):
        #try:
            # item = models.    


# Abstract model representing a "selected" product in a cart or order
class SelectedProduct(models.Model):
    #description = CharField(_("Description"), max_length=2000)
    quantity = models.IntegerField(_("Quantity"), default=0)
    unit_price = fields.MoneyField(_("Unit price"), default=Decimal("0"))
    total_price = fields.MoneyField(_("Total price"), default=Decimal("0"))
    
    class Meta:
        abstract = True

    def __str__(self):
        return ""

    def save(self, *args, **kwargs):
        # Set total price based on given quantity. 
        # If quantity is zero, delete it
        if not self.id or self.quantity > 0:
            self.total_price = self.unit_price * self.quantity
            super(SelectedProduct, self).save(*args, **kwargs)
        else:
            self.delete()
            
            
            
class CartItem(SelectedProduct):
    cart = models.ForeignKey("Cart", related_name="items", on_delete=models.CASCADE)
    url = CharField(max_length=2000)
    image = CharField(max_length=200, null=True)
    
    def get_absolute_url(self):
        return self.url

    def save(self, *args, **kwargs):
        super(CartItem, self).save(*args, **kwargs)

        # Check if this is the last cart item being removed
        if self.quantity == 0 and not self.cart.items.exists():
            self.cart.delete()