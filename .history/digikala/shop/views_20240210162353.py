from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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
        pasword=request.POST['password']
        user = authenticate(request, username=username,pasword=pasword)
        if user is not None:
            login(request,user)
            messages.success(request,("با موفقیت وارد شدید"))
            return redirect("home")
        
    else:
        return render(request, 'login.html')
def logout_user(request):
    logout(request)
    messages.success(request,("با موفقیت خارج شدید"))
    return redirect("home")
    