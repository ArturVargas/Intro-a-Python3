from django.contrib import admin
from .models import Product, Offer

#Para modificar las columnas que muestra la tabla en admin
class ProductAdmin(admin.ModelAdmin):
  list_display = ('product_name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
  list_display = ('code', 'discount')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
