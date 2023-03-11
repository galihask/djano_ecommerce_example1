from django.contrib import admin
from .models import Product, Cart, ProductCart, Category

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductCart)
admin.site.register(Category)
