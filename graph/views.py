from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import GraphData

@login_required
def graph_view(request):
    g_data = GraphData.objects.first()

    weight_data = [float(x) for x in g_data.weight.split("#")]
    protein_data = [float(x) for x in g_data.protein.split("#")]
    calorie_data = [float(x) for x in g_data.calories.split("#")]
    labels = [x for x in range(1, len(weight_data))]

    context = {
        'labels': labels,
        'weight': weight_data,
        'protein': protein_data,
        'calories': calorie_data,
    }

    return render(request, 'graph/graph_view.html', { 'data': context, 'title': User.username })

@login_required
def about(request):
    return render(request, 'graph/about.html', {'title': 'About'})

@login_required
def help(request):
    return render(request, 'graph/help.html', {'title': 'Help'})