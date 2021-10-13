from django.db import models


class Categorie(models.Model):
    cat_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_Name

    @staticmethod
    def get_get_all_categories():
        return Categorie.objects.all()

