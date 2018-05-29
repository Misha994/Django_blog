from django.shortcuts import redirect
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Article,Comments
from .forms import CommentForm,ArticleForm
from django.contrib import auth

def articles(request):
    return render_to_response('articles.html',{'articles': Article.objects.all(), 'username': auth.get_user(request).username})

def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

def addcomment(request, article_id):
    if request.POST:
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article=Article.objects.get(id=article_id)
            form.save()
    return redirect('/article/get/%s/'% article_id)

def addarticle(request):
    article_form = ArticleForm
    args = {}
    args['form'] = article_form
    args['username'] = auth.get_user(request).username
    if request.POST:
        form=ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
    return render_to_response('addarticle.html',args)