from rest_framework import serializers
from .models import Customer, Product, Sale

class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('product_id', 'product_name', 'price', 'company_name', 'description', 'is_available')

class CustomerSerializer(serializers.ModelSerializer):
   
        class Meta:
            model = Customer
            fields = ('customer_id', 'full_name', 'address', 'email', 'phone_no')

class SaleSerializer(serializers.ModelSerializer):
        product = ProductSerializer() 
        customer = CustomerSerializer()

        class Meta:
            model = Sale
            fields = ('id', 'product', 'customer','quantity', 'total', 'sale_date') 
