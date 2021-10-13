from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'store/login.html')

    def post(self, request):
        # Email-Password-Verification
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        customer = Customer.getAllEmails(email)
        error_message = None
        success_message = None
        if customer:
            flag = check_password(password, customer.password)
            request.session['email'] = customer.email
            request.session['customer_id'] = customer.id
            request.session['customer_is_login'] = customer.id
            if flag:
                print("Login SuccessFul.......")
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('HomePage')
            else:
                error_message = "Email or Password invalid !! Try Again !!"
        else:
            error_message = "Email or Password invalid !! Try Again !!"
        return render(request, 'store/login.html', {'error': error_message})


def logOut(request):
    request.session.clear()
    return redirect('login')
