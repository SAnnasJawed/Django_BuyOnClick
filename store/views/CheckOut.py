from django.shortcuts import render, redirect
from django.views import View

from store.models import Customer
from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')  # requesting and holding the address in a variable from POST dict
        phone = request.POST.get('phone')  # requesting and holding the phone in a variable from POST dict
        customer = request.session.get(
            'customer_id')  # requesting and holding the customer_id in a variable from session dict
        cart = request.session.get('cart')  # requesting and holding the cart in a variable from POST dict
        products = Product.get_products_by_id(
            list(cart.keys()))  # making a list of all the ids and getting products by id and holding them in a variable
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(ordered_customer=Customer(id = customer),
                          ordered_product_name=product,
                          price=product.product_Price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.placeOrder()  # saving order by calling the method(constructor we created)
            request.session['cart'] = {}  # requesting cart from session and clearing it

        return redirect('cart')
