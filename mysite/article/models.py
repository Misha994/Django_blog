from django.db import models


class Article(models.Model):
    # Set the name for the table in the database
    class Meta():
        db_table = "article"

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)
