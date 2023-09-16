from django.urls import path
from . import views

urlpatterns = [
    path('', views.graph_view, name='graph-view'),
    path('about/', views.about, name='graph-about'),
    path('help/', views.help, name='graph-help'),
]