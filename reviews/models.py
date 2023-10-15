from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from movies.models import Movie



class Review(models.Model):
    movie = models.ForeignKey(
        Movie, 
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.ImageField(
        validators=[
            MinLengthValidator(0, 'Avaliação não pode ser inferior a 0'),
            MaxLengthValidator(5, 'Avaliação não pode ser superior a 5'),
        ]
    )
    comment = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.movie