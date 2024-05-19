from django.urls import path
from . import views 

urlpatterns = [
    path('movie_list/', views.MovieListView.as_view()),
    path('movie/<str:title>/', views.MovieView.as_view()),
    path('images/<str:image_title>/', views.imagePage),
    path('trailers/<str:trailer_title>/', views.trailerPage),
    path('average_rating/<str:title>/', views.getAverageRating),
    path('ratemovie/<str:title>/', views.rateMovie),
]
