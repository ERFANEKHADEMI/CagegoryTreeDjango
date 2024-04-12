from django.contrib import admin
from django.urls import path, include
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('<path:categories>/', views.menu, name='menu'),
    path('', views.menu, name='menu'),
]
