from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import DataForm
from feed.models import Post

DATA_CHAR_SPLICE = '#'


@login_required
def graph_view(request):
    current_user = request.user

    if request.method == 'POST':
        data_form = DataForm(request.POST)
        if data_form.is_valid():

            weight = str(data_form.cleaned_data['weight'])
            protein = data_form.cleaned_data['protein']
            calories = data_form.cleaned_data['calories']

            current_user.profile.weight += DATA_CHAR_SPLICE + str(weight)
            current_user.profile.protein += DATA_CHAR_SPLICE + str(protein)
            current_user.profile.calories += DATA_CHAR_SPLICE + str(calories)

            current_user.save()

            post_content = data_form.cleaned_data['message']
            post_day = len(current_user.profile.calories.split(DATA_CHAR_SPLICE))
            post_data = {
                'weight': weight,
                'protein': protein,
                'calories': calories
            }
            Post.objects.create(content=post_content, day=post_day, data=post_data, author=current_user)

            messages.success(request, f'You successfully added data!')
            return redirect('graph-view')
    else:
        data_form = DataForm()

    if current_user.profile.weight == '':
        weight_data = [0]
        protein_data = [0]
        calorie_data = [0]
    else:
        weight_data = [float(x) for x in current_user.profile.weight.split(DATA_CHAR_SPLICE)]
        protein_data = [float(x) for x in current_user.profile.protein.split(DATA_CHAR_SPLICE)]
        calorie_data = [float(x) / 10 for x in current_user.profile.calories.split(DATA_CHAR_SPLICE)]
    labels = [x for x in range(1, len(weight_data) + 1)]

    context = {
        'title': current_user.username,
        'labels': labels,
        'weight': weight_data,
        'protein': protein_data,
        'calories': calorie_data,
        'data_form': data_form,
    }

    return render(request, 'graph/graph_view.html', context)


@login_required
def about(request):
    return render(request, 'graph/about.html', {'title': 'About'})


@login_required
def help(request):
    return render(request, 'graph/help.html', {'title': 'Help'})