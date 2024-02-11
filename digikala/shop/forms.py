
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':"form_control" , 'placeholder':"نام خود را وارد کنید"})
    )
    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':"form_control" , 'placeholder':"نام خانوادگی خود را وارد کنید"})
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class':"form_control" , 'placeholder':"ایمیل خود را وارد کنید"})
    )
    username =forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class':"form_control" , 'placeholder':"نام کاربری خود را وارد کنید"})
    )
    password1 =forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
            'class':"form_control" ,
            'name':'password',
            'type':'password',
            'placeholder':"رمز بالای 8 رقمی خود را وارد کنید"
            }
        )
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class':"form_control" ,
                'name':'password',
                'type':'password',
                'placeholder':" دوباره رمز بالای 8 رقمی خود را وارد کنید"
            }
        )
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
    