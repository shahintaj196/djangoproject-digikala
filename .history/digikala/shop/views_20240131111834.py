from django.shortcuts import render, HttpResponse

# Create your views here.


def helloworld(request):
    return HttpResponse('به فروشگاه من خوش آمدید')