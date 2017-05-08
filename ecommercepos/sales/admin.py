from django.contrib import admin
from .models import Product, Customer, Sale
# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Sale)
