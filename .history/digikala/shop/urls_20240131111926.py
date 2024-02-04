
from django.contrib import admin
from django.urls import path
from . import v

urlpatterns = [
    path('admin/', admin.site.urls),
]
