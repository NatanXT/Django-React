from django.contrib import admin
from .models import *
from .models import Order 



admin.site.register(Product)
admin.site.register(Review)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Order)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=[
        "user","createdAt","totalPrice"
    ]











# Register your models here.
