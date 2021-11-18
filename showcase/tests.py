# showcase/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Article
import datetime
# Create your tests here.
class ArticleTests(TestCase):

	def setUp(self):
		self.user=get_user_model().objects.create_user(
				username='testuser',
				email='test@email.com',
				password='secret'
			)

		self.article=Article.objects.create(
				title='A good title',
				subtitle='Test',
				body='Nice body content',
				date= datetime.date(2021, 11, 18),
				author=self.user,
			)

	def test_string_representation(self):
		article = Article(title='A sample title')
		self.assertEqual(str(article), article.title)

	def test_article_content(self):
		self.assertEqual(f'{self.article.title}', 'A good title')
		self.assertEqual(f'{self.article.subtitle}', 'Test')
		self.assertEqual(f'{self.article.author}', 'testuser')
		self.assertEqual(f'{self.article.body}', 'Nice body content')

	def test_article_list_view(self):
		response = self.client.get(reverse('showcase'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Nice body content')
		self.assertTemplateUsed(response, 'showcase.html')

	def test_article_detail_view(self):
		response = self.client.get('/article/1/')
		no_response = self.client.get('/article/100000/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'A good title')
		self.assertTemplateUsed(response, 'article_detail.html')





