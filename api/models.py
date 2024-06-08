from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MovieModel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='api/images')
    trailer = models.FileField(upload_to='api/trailers', default='')

    def __str__(self) -> str:
        return self.title






class RatingModel(models.Model):
    movie = models.ForeignKey("MovieModel", on_delete=models.CASCADE)
    BAD = 0.5
    BAD_PLUS = 1
    POOR = 1.5
    POOR_PLUS = 2
    OK = 2.5
    OK_PLUS = 3
    GOOD = 3.5
    GOOD_PLUS = 4
    EXCELLENT = 4.5
    EXCELLENT_PLUS = 5
    
    RATING_CHOICES = [
        (BAD, 'Bad'),
        (BAD_PLUS, 'Bad+'),
        (POOR, 'Poor'),
        (POOR_PLUS, 'Poor+'),
        (OK, 'Ok'),
        (OK_PLUS, 'Ok+'),
        (GOOD, 'Good'),
        (GOOD_PLUS, 'Good+'),
        (EXCELLENT, 'Excellent'),
        (EXCELLENT_PLUS, 'Excellent+'),
    ]

    @classmethod
    def is_value_in_rating_choices(cls, value):
        for rating in cls.RATING_CHOICES:
            if rating[0] == value:
                return True
            print(value, rating[0])
        return False

    rating = models.DecimalField(choices=RATING_CHOICES, max_digits=2, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.movie.title} {self.user} {self.rating}"