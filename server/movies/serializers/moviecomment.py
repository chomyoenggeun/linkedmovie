from rest_framework import serializers
from ..models import MovieComment, MovieReview
from django.contrib.auth import get_user_model

class MovieCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieComment
        fields = ('id', 'content', 'created_at', 'updated_at')
        read_only_fields = ('moviereview', 'user',)
    