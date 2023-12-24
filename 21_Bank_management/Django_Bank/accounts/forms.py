from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserBankAccountModel, UserAddressModel

ACCOUNT_TYPE = (
    # ('frontend', 'backend'),
    ('Savings', 'Savings'),
    ('Current', 'Current'),
)
GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class UserRegistrationForm(UserCreationForm):
    birth_day  =forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    
    street_address = forms.CharField(max_length = 100)
    city = forms.CharField(max_length = 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length = 100)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',  'account_type','birth_day', 'gender', 'street_address', 'city', 'postal_code', 'country']
        
        
    # jehetu ak e form the tinta model a data save hobe .. so save function ta handel korte hobbe.
    
    def save(self, commit= True):
        user =  super().save(commit=False)
        if commit == True:
            user.save() # user model a data dave hobe
            
            account_type = self.cleaned_data.get('account_type')
            birth_day = self.cleaned_data.get('birth_day')
            gender = self.cleaned_data.get('gender')
            street_address = self.cleaned_data.get('street_address')
            city = self.cleaned_data.get('city')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            
            UserAddressModel.objects.create(
                user = user,
                street_address = street_address,
                city = city,
                postal_code = postal_code,
                country = country,
            )
            
            UserBankAccountModel.objects.create(
                user = user,
                account_type = account_type,
                birth_day=birth_day, 
                gender = gender, 
                account_no = 1000000 + user.id
            )
            
        return user
    
    
    # Backend theke inputfield a style. tailwind css ar style class .
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
