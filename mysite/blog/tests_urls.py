
from django.test import TestCase
from django.urls import reverse
from .models import Category, Post

class UrlsTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.cat = Category.objects.create(name='Тестова', description='Опис тестової категорії')
        cls.post = Post.objects.create(
            title='Тестовий пост',
            content='Контент тестового посту',
            category=cls.cat,
            slug='test-post'
        )

    def test_index_url(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_list_url(self):
        url = reverse('article_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        url = reverse('article_category_list', args=[self.cat.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url(self):
        url = reverse('article_detail', args=[self.post.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
