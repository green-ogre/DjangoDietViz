from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='graph-home'),
    path('about/', views.about, name='graph-about'),
    path('help/', views.help, name='graph-help'),
]