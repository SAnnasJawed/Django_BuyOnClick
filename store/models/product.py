from django.db import models
from .category import Categorie


class Product(models.Model):
    product_Name = models.CharField(max_length=50)
    product_Price = models.IntegerField(default=0)
    product_Description = models.CharField(max_length=200, default='')
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    product_Image = models.ImageField(upload_to='media/store/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
