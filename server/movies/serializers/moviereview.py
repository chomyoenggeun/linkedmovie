from rest_framework import serializers
from ..models import MovieReview, Movie
from django.contrib.auth import get_user_model

class MovieReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = '__all__'
        read_only_fields = ('user',)

class MovieReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieReview
        fields = '__all__'
        depth = 1
        read_only_fields = ('user', 'like_users',)


