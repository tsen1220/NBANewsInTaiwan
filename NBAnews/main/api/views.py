from .serializers import ArticleSerializer
from main.models import news
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ArticleListView(ListCreateAPIView):
    queryset = news.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = news.objects.all()
    serializer_class = ArticleSerializer
