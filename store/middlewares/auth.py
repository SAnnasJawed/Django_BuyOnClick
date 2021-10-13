from django.shortcuts import render, redirect


def auth_middleware(get_response):
    def middleware(request):
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        print(request.session.get('customer_id'))
        if not request.session.get('customer_id'):
            return redirect(f'login?return_url={returnUrl}')
        print('middleware is working')
        response = get_response(request)
        return response

    return middleware
