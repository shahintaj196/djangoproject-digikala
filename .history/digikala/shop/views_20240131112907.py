from django.shortcuts import render, HttpResponse

# Create your views here.


def helloworld(request):
    return HttpResponse('<hبه فروشگاه من خوش آمدید')