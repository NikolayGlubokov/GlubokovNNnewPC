from django.contrib import admin
from .models import ProductCategory, Product,Basket


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'price', 'quantity')
    list_display_links = ('id', 'name')

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Basket)


