from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Categorie
from django.views import View


# Create your views here.

class Index(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart')
        remove_cart_item = request.POST.get('remove_cart_item')
        if cart:
            quantity_of_product = cart.get(product_id)
            if quantity_of_product:
                if remove_cart_item:
                    if quantity_of_product <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity_of_product - 1
                else:
                    cart[product_id] = quantity_of_product + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        print("cart", cart)
        return redirect('HomePage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        categories = Categorie.get_get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            Products = Product.get_all_products_by_categoryid(categoryID)
        else:
            Products = Product.get_all_products()
        context = {'Products': Products, 'categories': categories}
        return render(request, 'store/index.html', context)
