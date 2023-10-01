from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'genre'
    
    def __str__(self) -> str:
        return self.name