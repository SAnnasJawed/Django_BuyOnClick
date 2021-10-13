from django import template
register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys_in_cart = cart.keys()
    for key in keys_in_cart:
        if int(key) == product.id:
            return True
    return False


@register.filter(name='quantity_of_product_in_cart')
def quantity_of_product_in_cart(product, cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
            return cart.get(key)


@register.filter(name='total_price')
def total_price(product, cart):
    return product.product_Price * quantity_of_product_in_cart(product, cart)


@register.filter(name='Total_Bill')
def Total_Bill(products, cart):
    sum = 0;
    for p in products:
        sum += total_price(p, cart)
    return sum


@register.filter(name='currency')
def currency(number):
    return 'RS: ' + str(number)


@register.filter(name='multiply')
def currency(number, num2):
    return number * num2