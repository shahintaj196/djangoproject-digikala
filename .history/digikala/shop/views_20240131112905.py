from django.shortcuts import render, HttpResponse

# Create your views here.


def helloworld(request):
    return HttpResponse('<hq=به فروشگاه من خوش آمدید')