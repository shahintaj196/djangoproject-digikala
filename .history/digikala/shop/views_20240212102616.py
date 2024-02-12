from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


# Create your views here.


def helloworld(request):
    all_Products = Product.objects.all()
    # return HttpResponse (all_Products)
    # return HttpResponse('<h1>به فروشگاه من خوش آمدید<h1/>')
    return render(request, 'index.html', {'products': all_Products})



def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request,user)
            messages.success(request,("با موفقیت وارد شدید"))
            return redirect("home")
        else:
            messages.success(request,("لاگین ب مشکل خورده"))
            return redirect("login")
            
    else:
        return render(request, 'login.html')
    
    
def logout_user(request):
    logout(request)
    messages.success(request,("با موفقیت خارج شدید"))
    return redirect("home")

def signup_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password1 )
            login(request, user)
            messages.success(request, ("اکانت شما ساخته شد"))
            return redirect("home")
        else:
            messages.success(request, ("اکانت شما ساخته نشد"))
            return redirect("signup")
    else:
        return render(request, 'signup.html', {'form':form})
    
    
def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request, 'product.html')
    
    