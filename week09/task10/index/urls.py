from django.urls import path,include

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login1/',views.login1, name='login1'),
]