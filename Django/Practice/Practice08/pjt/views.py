from django.shortcuts import render
from articles.models import Article


def index(request):
    articles = Article.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "index.html", context)
