import datetime

from django.shortcuts import render, redirect

from .models import Article, Comment


def home(request):
    content = Article.objects.order_by('-pub_date')[:10]
    if articles:
        context = {
            'title': 'Home',
            'content': content,
            }
    return render(request, 'home.html', context)


def articles(request):
    content = Article.objects.order_by('-pub_date')[:10]
    if content:
        context = {
            'title': 'Articles',
            'content': content,
            }
    else:
        context = {
        'title': 'Article'
        }
    return render(request, 'articles.html', context)


def article_view(request, title):
        art = Article.objects.get(title=title)
        comments = art.comment_set.all()[:6]
        if request.method == 'POST':
            data = request.POST.copy()
            if data:
                comment = data.get('comment')
                if comment:
                    c = Comment(article=art, date=datetime.date.today(), comment=comment)
                    c.save()
        context = {
            'article': art,
            'title': title,
            'comments': comments,
            }
        return render(request, 'article.html', context)


def about(request):
    context = {
        'title': 'About',
        }
    return render(request, 'about.html', context)
