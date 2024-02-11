from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    first_name =  forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':"form_control" , 'placeholder':"نام خود را وارد کنید"})
    )
    last_name =  forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':"form_control" , 'placeholder':"نام خانوادگی خود را وارد کنید"})
    )
       first_name =  forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':"form_control" , 'placeholder':"نام خود را وارد کنید"})
    )