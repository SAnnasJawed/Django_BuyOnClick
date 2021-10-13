from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):
        list_of_all_ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(list_of_all_ids)
        return render(request, 'store/cart.html', {'products': products})
