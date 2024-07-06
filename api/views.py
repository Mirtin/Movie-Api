from django.http import HttpResponse, FileResponse
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
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
@permission_classes([AllowAny])
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
    user = request.user
    rating = float(request.data.get("rating", 0))
    
    try:
        movie = MovieModel.objects.get(title=title)
    except MovieModel.DoesNotExist:
        return Response({"msg": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if RatingModel.is_value_in_rating_choices(rating):
        RatingModel.objects.update_or_create(movie=movie, user=user, defaults={"rating": rating})
        response = {"msg": "Rating created/updated"}
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {
            "msg": "Invalid rating value",
            "data": {
                "rating": rating,
                "title": title,
            }
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def getRatedMovies(request):
    user = request.user
    print(user, ' the user')
    rated_movies = RatingModel.objects.filter(user=user)
    response = {"rate_movies": rated_movies}
    return Response(response)

