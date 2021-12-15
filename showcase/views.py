#showcase/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Article
import datetime 
# Create your views here.

class ArticleListView(ListView):
	model = Article 
	template_name = 'showcase.html'

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'article_detail.html'

class ArticleCreateView(CreateView):	
	model = Article 
	template_name = 'article_new.html'
	fields = ['title', 'author', 'body', 'subtitle' ]

class ArticleUpdateView(UpdateView):
	model = Article
	template_name = 'article_edit.html'
	fields = ['title','body','subtitle']

class ArticleDeleteView(DeleteView):
	model = Article 
	template_name = 'article_delete.html'
	success_url = reverse_lazy('showcase')


