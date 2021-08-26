from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', views.home, name="home"),
    path('', include('products.urls')),
]
urlpatterns += staticfiles_urlpatterns()