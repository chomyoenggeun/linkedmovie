from rest_framework import serializers
from ..models import MovieReview, Movie, Genre

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
        read_only_fields = ('title','genres')


class AddRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieReview
        fields=['rank']