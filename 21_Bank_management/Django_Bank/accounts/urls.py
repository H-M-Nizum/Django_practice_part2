from django.urls import path
from . import views

urlpatterns = [
   path('register/',  views.UserRegistrationViews.as_view(), name='register')
]
