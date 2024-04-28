from django.http import HttpResponse, FileResponse

from rest_framework.pagination import PageNumberPagination 
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import MovieModel

from .serializers import MovieSerializer


class MoviePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class MovieListView(ListAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination



class MovieView(RetrieveAPIView):
    serializer_class = MovieSerializer
    lookup_field = 'title'
    queryset = MovieModel.objects.all()


def imagePage(request, image_title):
    image_data = open(f"api/images/{image_title}", "rb").read()
    
    return HttpResponse(image_data, content_type="image/png")

def trailerPage(request, trailer_title):
    trailer_data = open(f"api/trailers/{trailer_title}", 'rb')
    return FileResponse(trailer_data, content_type='video/mp4')