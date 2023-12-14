from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def add_categories(request):
    if request.method == 'POST':
        categories_form = forms.CategoryForm(request.POST)
        if categories_form.is_valid():
            categories_form.save()
            return redirect('add_categories')
    else:
        categories_form = forms.CategoryForm()
    return render(request, 'add_categories.html', {'form': categories_form})