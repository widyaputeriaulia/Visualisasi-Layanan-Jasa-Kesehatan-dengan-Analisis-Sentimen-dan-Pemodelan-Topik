"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
 
urlpatterns = [
    url(r'^$', views.index),
    url('bethesda/', views.index01),
    url('jih/', views.index02),
    url('kota/', views.index03),
    url('panembahan/', views.index04),
    url('panti_rapih/', views.index05),
    url('pau_hardjolukito/', views.index06),
    url('pku_muhammadiyah/', views.index07),
    url('sardjito/', views.index08),
    url('sleman/', views.index09),
    url('ugm/', views.index010),
    url('wates/', views.index011),

]
