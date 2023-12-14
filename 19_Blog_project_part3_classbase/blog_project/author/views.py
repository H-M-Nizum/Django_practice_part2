from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

# for check login or not
from django.contrib.auth.decorators import login_required
from posts.models import Post

# for class base user login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Create your views here.

# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'add_author.html', {'form': author_form})


def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('user_login')
        
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'register'})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
           user_name = form.cleaned_data['username']
           user_pass = form.cleaned_data['password']
           user = authenticate(username = user_name, password=user_pass)
           
           if user is not None:
               messages.success(request, 'Loged in successfully')
               login(request, user)
               return redirect('user_profile')
           
           
           else:
                messages.warning(request, 'login information incorrect')
                return redirect('user_login')
            
        else:
            messages.warning(request, 'not a valid user')
            return redirect('home')
            
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form': form, 'type': 'Login'})


#  class base login view
class user_login_view(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('user_profile')
    
    def get_success_url(self):
        return reverse_lazy('user_profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'User login successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'User login information is incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
    

   
            
@login_required    
def profileupdate(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data':data})


@login_required    
def edit_profile(request):
    if request.method == 'POST':
        profile_form = PasswordChangeForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Update profile successfully')
            return redirect('user_profile')
        
    else:
        profile_form = forms.updateProfileForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': profile_form})



def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'password update successfully')
            return redirect('user_profile')
        
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')

# class base user logout
class user_logout_view(LogoutView):
    def get_success_url(self):
        return reverse_lazy('user_login')