from django.db import models

# Create your models here.


class MovieModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='api/images')

    def __str__(self) -> str:
        return self.title