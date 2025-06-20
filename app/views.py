from app.models import Article
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

def home(request):
    articles = Article.objects.all()
    return render(request, "app/home.html", {"articles": articles})

class ArticleCreateView(CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "twitter_post"]
    success_url = reverse_lazy("home") 