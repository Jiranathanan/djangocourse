from app.models import Article
from django.http import HttpResponse

def home(request):
    articles = Article.objects.all()

