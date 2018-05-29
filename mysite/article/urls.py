from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all/$', views.articles),
    url(r'^get/(?P<article_id>\d+)/$', views.article),
    url(r'^addcomment/(?P<article_id>\d+)/$', views.addcomment),
    url(r'^addarticle/$', views.addarticle),
    url(r'^$', views.articles),

]