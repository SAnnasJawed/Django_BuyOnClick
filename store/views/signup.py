from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'store/signup.html')

    def post(self, request):
        # On Post request registration
        postData = request.POST
        first_Name = postData.get('firstname')
        last_Name = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        phone = postData.get('phonenumber')

        details = {
            'first_Name': first_Name,
            'last_Name': last_Name,
            'email': email,
            'phone': phone
        }
        customer = Customer(first_Name=first_Name,
                            last_Name=last_Name,
                            email=email,
                            password=password,
                            phone=phone)

        # Validation
        def validateCustomer(customer):
            error_message = None

            if not customer.first_Name:
                error_message = "First Name Required !!"
            elif len(customer.first_Name) < 3:
                error_message = "First Name must be atleast 3 char long !!"
            elif not customer.last_Name:
                error_message = "Last Name Required !!"
            elif len(customer.last_Name) < 3:
                error_message = "Last Name must be atleast 3 char long !!"
            elif not customer.password:
                error_message = "Please enter a password !!"
            elif len(customer.password) < 5:
                error_message = "Password must be atleast 5 char long !!"
            elif not customer.phone:
                error_message = "Please enter a phone number !!"
            elif len(customer.phone) < 10:
                error_message = "Phone number cannot be less than 10 digits !!"
            elif len(customer.phone) > 15:
                error_message = "Phone number cannot be greater than 15 digits !!"
            elif customer.isExists():
                error_message = "Email Already registered !!"

            return error_message

        error_message = validateCustomer(customer)

        # Saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            context = {
                'details': details,
                'error': error_message
            }
            return render(request, 'store/signup.html', context)
