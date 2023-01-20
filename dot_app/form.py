from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
# from phone_field import PhoneField
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.contrib.auth.models import User, Group, Permission

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name= forms.CharField(max_length=100,required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(max_length=100,required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    email= forms.EmailField(max_length=100,required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_staff= forms.BooleanField(required=False,
                                      initial=False,
                                      label='')
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2', 'is_staff','groups']
    groups = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        to_field_name='id',
       
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class EntrollmentForm(UserCreationForm):
    username = forms.CharField(max_length=100,required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name= forms.CharField(max_length=100,required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(max_length=100,required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    email= forms.EmailField(max_length=100,required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_staff= forms.BooleanField(required=False,
                                      initial=False,
                                      label='')
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2', 'is_staff','groups']
    groups = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        to_field_name='id',
       
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class AddHotelsForm(UserCreationForm):

    username = forms.CharField(max_length=100,required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'password']
    # groups = forms.ModelChoiceField(
    #     queryset=Group.objects.all(),
    #     to_field_name='id',
       
    #     required=True,  
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )

# class AddHotelsForm(forms.ModelForm):
#     hotel_type = forms.ChoiceField(
#                                 widget=forms.TextInput)
#     name = forms.CharField(max_length=100,required=True,
#                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
#     contact_person = forms.CharField(max_length=100,required=True,
#                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
#     contact_number = forms.CharField(max_length=100,required=True,
#                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
#     username = forms.CharField(max_length=100,required=True,
#                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     address = forms.CharField(max_length=100,required=True,
#                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
#     country = forms.ChoiceField(
#                                 widget=forms.TextInput)
#     state = forms.ChoiceField(
#                                 widget=forms.TextInput)
#     city = forms.ChoiceField(
#                                 widget=forms.TextInput)

#     class Meta:
#         model = User
#         fields = ['username','first_name', 'password','groups']
#     groups = forms.ModelChoiceField(
#         queryset=Group.objects.all(),
#         to_field_name='id',
       
#         required=True,  
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
