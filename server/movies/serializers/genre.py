from rest_framework import serializers
from ..models import Genre, MovieGenre


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('id', 'name',)


class MovieGenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovieGenre
        fields = '__all__'