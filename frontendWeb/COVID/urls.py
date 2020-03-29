from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='COVID19-home'),
    path('about/', views.about, name='COVID19-about'),
]