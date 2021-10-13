from django.db import models


class Customer(models.Model):
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    @staticmethod
    def getAllEmails(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
