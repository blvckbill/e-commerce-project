from django.contrib import admin
from .models import Order, Customer, Product, OrderItem, ShippingAddress
# Register your models here.
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)