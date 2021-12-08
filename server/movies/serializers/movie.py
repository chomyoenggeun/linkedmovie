from rest_framework import serializers
from ..models import MovieReview, Movie, Genre, MovieLike
from django.contrib.auth import get_user_model
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from accounts.models import User



class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'title',)



class MovieSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('pk', 'movie_id',),


    class MovieReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = MovieReview
            fields = ('pk', 'movie_id',),


    genre = GenreSerializer(many=True, read_only=True)
    review = MovieReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'



class MovieLikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('movie_pk', 'like_users',)
        read_only_fields = ('__all__',)

    class Meta:
        model = User
        fields = ('__all__')
        read_only_fields = ('password', 'username')


class AddRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieReview
        fields=['rank']