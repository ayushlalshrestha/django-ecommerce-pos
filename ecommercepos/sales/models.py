from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(primary_key = True, max_length = 200, unique = True, null = False)
    product_name = models.CharField(max_length = 200)
    price = models.IntegerField(default = 00)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    is_available = models.BooleanField(default = True, verbose_name = "Availability ?")
    
    def __str__(self):
        return self.product_id + " - "+self.product_name


class Customer(models.Model):
    customer_id = models.CharField(primary_key = True, max_length=255, unique = True, null = False)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    
    def __str__(self):
        return self.customer_id + " " + self.full_name

class Sale(models.Model):
    product = models.ForeignKey(Product)
    customer = models.ForeignKey(Customer)
    sale_date = models.DateTimeField(auto_now_add = True)
    quantity = models.IntegerField(null = False)
    total = models.IntegerField(null = False)

    def __str__(self):
        return self.sale_date

        