from django.test import TestCase
from .forms import *


class Article_Form_Test(TestCase):

    def test_CommentForm_valid(self):
        form = CommentForm(data={'comments_text': 'testtext'})
        self.assertTrue(form.is_valid())

    def test_ArticleForm_valid(self):
        form = ArticleForm(data={'article_title': 'title',
                                 'article_text': 'article_text',
                                 'article_date': '2000-01-01'})
        self.assertTrue(form.is_valid())

    def test_ArticleForm_invalid(self):
        form = ArticleForm(data={'article_title': 'title',
                                 'article_text': 'article_text',
                                 'article_date': ''})
        self.assertFalse(form.is_valid())
