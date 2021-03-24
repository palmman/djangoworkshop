from django.contrib import admin
from store.models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created', 'updated' ]
    list_editable = [ 'price', 'stock']
    list_per_page = 2

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'total', 'token', 'created', 'updated' ]
    list_per_page = 2

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'created', 'updated']
    list_per_page = 2

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
