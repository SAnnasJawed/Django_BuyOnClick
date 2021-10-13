import datetime

from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    ordered_product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    completed = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()
        return 'Saved Successfully'

    @staticmethod
    def fetch_orders_by_customers_id(customer_id):
        return Order\
            .objects\
            .filter(ordered_customer=customer_id)\
            .order_by('date')
