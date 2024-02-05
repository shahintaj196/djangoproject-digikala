from django.shortcuts import render, HttpResponse
 from .models import Product

# Create your views here.


def helloworld(request):
    all_Products = Product.objects.
    # return HttpResponse('<h1>به فروشگاه من خوش آمدید<h1/>')
    return render(request, 'index.html')