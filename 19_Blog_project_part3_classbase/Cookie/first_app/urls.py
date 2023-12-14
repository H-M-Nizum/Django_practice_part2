from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('get/',views.get_cookie, name='get_cookie'),
    path('delete/',views.delete_cookies, name='delete_cookies'),
]
