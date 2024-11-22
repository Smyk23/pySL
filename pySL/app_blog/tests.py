from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleCategoryList, ArticleList, ArticleDetail


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, 
                         HomePageView)

class ArticleCategoryListTests(TestCase):
    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_category_url_resolve_view(self):
        view = resolve('/articles/category/name')
        self.assertEqual(view.func.view_class,
                         ArticleCategoryList)

class ArticleListTests(TestCase):
    def test_articleList_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_articleList_url_resolve_view(self):
        view = resolve('/articles')
        self.assertEqual(view.func.view_class,
                         ArticleList)

class ArticleDetailTests(TestCase):
    
    def test_articleList_url_resolve_view(self):
        view = resolve('/articles/n/a/m/e')
        self.assertEqual(view.func.view_class,
                         ArticleDetail)
