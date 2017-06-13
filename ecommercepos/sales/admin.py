from django.contrib import admin
from .models import Product, Customer, Sale
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    list_display = ('product_id', 'product_name', 'price', 'company_name', 'is_available',)
    list_editable = ('price', 'is_available', )
    list_filter = ('company_name','is_available', )

    search_fields = ('product_name', 'company_name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Sale)
