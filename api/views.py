from django.http import HttpResponse, FileResponse
from django.db.models import Avg

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination 
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import MovieModel, RatingModel

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









@api_view(['GET'])
def getAverageRating(request, title):
    average_rating = RatingModel.objects.filter(movie__title=title).aggregate(avg_rating=Avg('rating'))
    if average_rating['avg_rating'] is not None:
        response = {
            'average_rating': average_rating['avg_rating']
        }
    else:
        response = {
            'message': 'No ratings yet for this movie.'
        }
    return Response(response)