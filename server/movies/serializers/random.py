from rest_framework import serializers
from ..models import Movie
from django.contrib.auth import get_user_model

class MovieRandomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'genres')
    