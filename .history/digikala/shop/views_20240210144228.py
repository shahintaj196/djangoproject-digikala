from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.


def helloworld(request):
    all_Products = Product.objects.all()
    # return HttpResponse (all_Products)
    # return HttpResponse('<h1>به فروشگاه من خوش آمدید<h1/>')
    return render(request, 'index.html', {'products': all_Products})



def about(request):
    return render(request, 'about.html')


def login_user(request)