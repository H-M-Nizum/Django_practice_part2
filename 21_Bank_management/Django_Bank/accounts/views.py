from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class UserRegistrationViews(FormView):
    template_name = 'user_regostration.html'
    form_class = UserRegistrationForm
    success_url =reverse_lazy('register')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid functions call hobe jodi sob thik thake
    
    
    
class Userloginviews(LoginView):
    template_name = 'user_login.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
class userlogoutview(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    

# profile view
class UserBankAccountUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})