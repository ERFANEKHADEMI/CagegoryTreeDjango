from django.contrib import admin
from django.urls import path, include
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:categories>/', views.menu, name='menu'),
]
