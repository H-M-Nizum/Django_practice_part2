from typing import Any
from django.shortcuts import render, redirect
from . import forms
from .import models 
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
# for class base view login required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required    
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})


# add post using class based views
# https://ccbv.co.uk/projects/Django/4.2/django.views.generic.edit/CreateView/
@method_decorator(login_required, name='dispatch')
class Addpostcreateview(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    #  reverse_lazy work like redirect
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


@login_required    
def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('user_profile')
    # else:
    #     post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})


# class based edit post
@method_decorator(login_required, name='dispatch')
class edit_post_view(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    # select primary key id
    pk_url_kwarg ='id'
    #  reverse_lazy work like redirect
    success_url = reverse_lazy('user_profile')




@login_required    
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    print(post)
    return redirect('home')



# class based delete post
# for delete post first create a template same to same add_post.html 
@method_decorator(login_required, name='dispatch')
class delete_post_view(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    #  reverse_lazy work like redirect
    success_url = reverse_lazy('user_profile')
    # select primary key id
    pk_url_kwarg ='id'



class post_details_view(DetailView):
    model  = models.Post
    # pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        post = self.object # post model ar object ekhan a store korlam
        comments = post.comments.all()

        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context        
            