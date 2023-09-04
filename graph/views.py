from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {}
    return render(request, 'graph/home.html', context)

def about(request):
    return render(request, 'graph/about.html', {'title': 'About'})

def help(request):
    return render(request, 'graph/help.html', {'title': 'Help'})