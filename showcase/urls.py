#showcase/urls.py
from django.urls import path
from .views import (
	ArticleListView, 
	ArticleDetailView, 
	ArticleCreateView,
	ArticleUpdateView,
	ArticleDeleteView,
)
urlpatterns = [
	path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
	path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
	path('article/new/', ArticleCreateView.as_view(), name='article_new'),
	path('article/<int:pk>/', ArticleDetailView.as_view(),
		name='article_detail' ),
	path('showcase/', ArticleListView.as_view(), name='showcase'),

]