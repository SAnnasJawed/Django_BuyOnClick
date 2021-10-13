from django import template
register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys_in_cart = cart.keys()
    for key in keys_in_cart:
        if int(key) == product.id:
            return True
    return False


@register.filter(name='currency')
def currency(number):
    return 'RS: ' + str(number)