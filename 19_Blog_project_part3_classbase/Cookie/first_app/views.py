from django.shortcuts import render

from datetime import datetime, timedelta
# Create your views here.

def home(request):
    response = render(request, 'home.html')
    # response.set_cookie('name', 'Rahim', max_age=10)
    # 7 days ar jonne cookie save hoye thakbe.
    response.set_cookie('name', 'Rahim', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request, 'get_cookie.html', {'name': name})


def delete_cookies(request):
    response = render(request, 'delete.html')
    response.delete_cookie('name')
    return response


#  session

def set_session(request):
    data = {
        'name' : 'Nizum',
        'age' : 23,
        'language' : 'bangla'
    }
    
    request.session.update(data)
    return render(request, 'home.html')


def get_session(request):
    data = request.session
    return render(request, 'get_session.html', {'data': data})


def delete_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delete_session.html')