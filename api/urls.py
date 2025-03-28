from django.urls import path
from . import views 

urlpatterns = [
    path('movie_list/', views.MovieListView.as_view()),
    path('movie/<str:title>/', views.MovieView.as_view()),
    path('images/<str:image_title>/', views.imagePage),
    path('trailers/<str:trailer_title>/', views.trailerPage),
    path('average_rating/<str:title>/', views.getAverageRating),
    path('rate_movie/<str:title>/', views.rateMovie),
    path('rated_movie/', views.RatedMovieView.as_view()),
    path('saved_movie/', views.SavedMovieView.as_view()),
    path('add_to_saved/<str:title>', views.addToSaved),
    path('remove_from_saved/<str:title>', views.removeFromSaved),
    path('is_saved/<str:title>/', views.isSaved)
]
