from django.contrib import admin
from .models import Genre, Movie, MovieGenre, MovieReview, MovieComment, MovieLike

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieGenre)
admin.site.register(MovieReview)
admin.site.register(MovieComment)
admin.site.register(MovieLike)