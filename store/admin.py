from django.contrib import admin
from .models.product import Product
from .models.category import Categorie
from .models.customer import Customer
from .models.orders import Order


# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['product_Name', 'product_Price', 'category', ]


class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_Name']


admin.site.register(Product, AdminProduct)
admin.site.register(Categorie, AdminCategory)


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_Name', 'last_Name', 'email']


admin.site.register(Customer, AdminCustomer)
admin.site.register(Order)
