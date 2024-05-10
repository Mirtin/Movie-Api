from django.contrib import admin
from .models import MovieModel, RatingModel

# Register your models here.

admin.site.register(MovieModel)
admin.site.register(RatingModel)