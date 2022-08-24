from django.db import models
from django.core import validators

# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70,verbose_name='Product Name')
    description = models.TextField(max_length=800,verbose_name='Description')
    price = models.FloatField(verbose_name='Price',
        validators=[validators.MinValueValidator(50),validators.MaxValueValidator(100000)])

    def __str__(self):
        return self.name


class OrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Can change as a Foreign Key to the user model
    customer_email = models.EmailField(verbose_name='Customer Email')
    product = models.ForeignKey(to=Product,verbose_name='Product',on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    # This field can be changed as status
    has_paid = models.BooleanField(default=False,verbose_name='Payment Status')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_email
        