from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
# Create your views here.

class UserRegistrationViews(FormView):
    template_name = 'user_regostration.html'
    form_class = UserRegistrationForm
    success_url =reverse_lazy('register')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid functions call hobe jodi sob thik thake
    