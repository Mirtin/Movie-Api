from django.http import HttpResponse, FileResponse
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination 
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import MovieModel, RatingModel

from .serializers import MovieSerializer

from .config import SECRET_KEY


class MoviePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000


class MovieListView(ListAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    permission_classes = (AllowAny,)


class MovieView(RetrieveAPIView):
    serializer_class = MovieSerializer
    lookup_field = "title"
    queryset = MovieModel.objects.all()
    permission_classes = (AllowAny,)






def imagePage(request, image_title):
    image_data = open(f"api/images/{image_title}", "rb")
    
    return HttpResponse(image_data, content_type="image/png")

def trailerPage(request, trailer_title):
    trailer_data = open(f"api/trailers/{trailer_title}", "rb")
    return FileResponse(trailer_data, content_type="video/mp4")









@api_view(["GET"])
def getAverageRating(request, title):
    movie_title = get_object_or_404(MovieModel, title=title)
    average_rating = RatingModel.objects.filter(movie__title=movie_title).aggregate(average_rating=Avg("rating"))
    if average_rating['average_rating'] is not None:
        response = {
            "average_rating": average_rating["average_rating"]
        }
    else:
        response = {
            "message": 'No ratings yet for this movie.'
        }
    return Response(response)


@api_view(["POST"])
def rateMovie(request, title):
    user = request.data.get('user', None)
    rating = float(request.data.get("rating", 0))
    secret_key = request.data.get("secret_key", None)
    if secret_key == SECRET_KEY and RatingModel.is_value_in_rating_choices(rating):
        movie_title = get_object_or_404(MovieModel, title=title)
        if RatingModel.objects.filter(movie=movie_title, user=user):
            RatingModel.objects.filter(movie=movie_title, user=user).delete()
        RatingModel.objects.create(movie=movie_title, user=user, rating=rating)

        response = {"msg": 'Object created'}
    else:
        response = {"msg": 'Wrong params',
                    "params": {
                        "user": user,
                        "rating": rating,
                        "title": title,
                    }}
    return Response(response)
