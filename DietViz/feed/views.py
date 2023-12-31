from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post