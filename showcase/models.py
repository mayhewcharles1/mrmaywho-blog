#showcase/models.py
from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	date = models.DateField()
	body = models.TextField()
	author = models.ForeignKey(
		'auth.User',
		on_delete=models.CASCADE,
		)
	body = models.TextField()

	def __str__(self):
		return self.title
