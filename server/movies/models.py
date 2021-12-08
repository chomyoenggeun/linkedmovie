from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')

    def __str__(self):
        return f'{self.pk}: {self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    backdrop_path = models.TextField(null=True, blank=True)
    
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    def __str__(self):
        return f'{self.pk}: {self.title}'


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre')


class MovieReview(models.Model):
    RANKS = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=100)
    movie_pk = models.IntegerField()
    rank = models.IntegerField(choices=RANKS, default=5)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies_like_reviews')

    def __str__(self):
        return self.title


class MovieComment(models.Model):
    moviereview = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
    content = models.TextField()
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content

class MovieLike(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moive_like')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies_like_users')
