from django.shortcuts import render, redirect
from django.views import View

from store.models import Customer
from store.models.product import Product
from store.models.orders import Order


class OrderView(View):
    def get(self, request):
        customer = request.session.get(
            'customer_id')  # requesting customer id from the session and holding it in a variable
        orders = Order.fetch_orders_by_customers_id(customer)
        orders = orders.reverse()
        return render(request, 'store/orders.html', {'orders': orders})
