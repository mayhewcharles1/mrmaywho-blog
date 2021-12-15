#showcase/models.py
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	date = models.DateField(auto_now_add=True)
	body = models.TextField()
	author = models.ForeignKey(
		'auth.User',
		on_delete=models.CASCADE,
		)
	body = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('article_detail', args=[str(self.id)])