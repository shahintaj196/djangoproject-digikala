from django.shortcuts import render, HttpResponse
 from .models import P

# Create your views here.


def helloworld(request):
    # return HttpResponse('<h1>به فروشگاه من خوش آمدید<h1/>')
    return render(request, 'index.html')