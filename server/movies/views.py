from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Movie, Genre, MovieReview, MovieComment, MovieGenre, MovieLike

from .serializers.movie import MovieSerializer, MovieListSerializer, MovieLikeSerializer
from .serializers.moviereview import MovieReviewSerializer, MovieReviewListSerializer
from .serializers.moviecomment import MovieCommentSerializer 
from .serializers.genre import GenreSerializer, MovieGenreSerializer
from .serializers.random import MovieRandomSerializer

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# from community.models import Review

# Create your views here.

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_list(request):
    # 인기순으로 영화 제목 보내기 (selectBox)
    if request.method == 'GET':
        movies = Movie.objects.order_by('-popularity')[:50]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    elif request.method =='POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data='delete successfully', status=status.HTTP_204_NO_CONTENT)




# 랜덤 영화
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def random(request):
    movies = Movie.objects.order_by('?')[:200]
    serializer = MovieRandomSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 장르 정보
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def genre(request):
    genre = Genre.objects.all()
    serializer = GenreSerializer(genre, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



######################################################

## 리뷰 part

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def moviereview_list(request):  
    if request.method == 'GET':
        moviereviews = get_list_or_404(MovieReview)
        serializer = MovieReviewListSerializer(moviereviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def moviereview_detail_update_delete(request, moviereview_pk):
    moviereview = get_object_or_404(MovieReview, pk=moviereview_pk)

    if request.method == 'GET':
        serializer = MovieReviewSerializer(moviereview)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # 해당 review의 작성자가 아닌 경우 review를 수정하거나 삭제하지 못하게 설정
        if not request.user.moviereview_set.filter(pk=moviereview_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

        moviereview.delete()
        data = {
            'delete': f'데이터 {moviereview_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = MovieReviewSerializer(moviereview, data=request.data)
        # 해당 review의 작성자가 아닌 경우 review를 수정하거나 삭제하지 못하게 설정
        if not request.user.moviereview_set.filter(pk=moviereview_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# # 댓글 part
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def moviecomment_create(request, moviereview_pk):
    moviereview = get_object_or_404(MovieReview, pk=moviereview_pk)
    if request.method == 'GET':
        moviecomments = moviereview.moviecomment_set.order_by('-pk')
        serializer = MovieCommentSerializer(moviecomments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(moviereview=moviereview, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def moviecomment_update_delete(request, moviecomment_pk):
    moviecomment = get_object_or_404(MovieComment, pk=moviecomment_pk)

    if request.method == 'GET':
        serializer = MovieCommentSerializer(moviecomment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieCommentSerializer(moviecomment, data=request.data)
        if not request.user.moviecomment_set.filter(pk=moviecomment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':        
        if not request.user.moviecomment_set.filter(pk=moviecomment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        moviecomment.delete()
        data = {
            'id': moviecomment_pk,
            'delete': f'data {moviecomment_pk} is deleted!!',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_likes(request, movie_id):
    movie = get_object_or_404(MovieLike, movie_id=movie_id)
    serializer = MovieLikeSerializer(movie)
    
    return Response(serializer.data)