"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from . import views


def homepage(request):
    return render(request, 'home.html')


def error_view(request):
    raise Exception("This is a test error")


urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('equipment/', include('equipment.urls'), name='equipment'),
    path('work_orders/', include('work_orders.urls')),
    path("accounts/", include("allauth.urls")),
    path("users/", include("users.urls")),
    path("error/", error_view)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler400 = views.custom_400
handler403 = views.custom_403
handler404 = views.custom_404
handler500 = views.custom_500
