from rest_framework import serializers
from .models import MovieModel, RatingModel


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = ['id', 'title', 'description', 'image', 'trailer']


class RatingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = RatingModel
        fields = ['movie']
