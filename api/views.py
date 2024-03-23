from django.shortcuts import render

from rest_framework.pagination import PageNumberPagination 
from rest_framework.generics import ListAPIView

from .models import MovieModel

from .serializers import MovieSerializer


class MoviePagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class MovieListView(ListAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination