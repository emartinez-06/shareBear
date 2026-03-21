from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('process/', views.process, name='process'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]