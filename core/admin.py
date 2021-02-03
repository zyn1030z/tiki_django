from django.contrib import admin

# Register your models here.
from core.models import CustomerUser, Category, Product, Order, OrderItem, ShippingAddress

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(CustomerUser)
