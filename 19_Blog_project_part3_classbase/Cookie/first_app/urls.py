from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name='home'),
    path('',views.set_session, name='home'),
    path('get/',views.get_cookie, name='get_cookie'),
    path('delete/',views.delete_cookies, name='delete_cookies'),
    path('deletes/',views.delete_session, name='delete_session'),
    path('get_s/',views.get_session, name='get_session'),
]
