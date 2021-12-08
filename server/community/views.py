from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Review, Comment

from .serializers import CommentSerializer, ReviewListSerializer, ReviewSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.

# 리뷰 part
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # 해당 review의 작성자가 아닌 경우 review를 수정하거나 삭제하지 못하게 설정
        if not request.user.review_set.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)
        review.delete()
        data = {
            'delete': f'데이터 {review_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        # 해당 review의 작성자가 아닌 경우 review를 수정하거나 삭제하지 못하게 설정
        if not request.user.review_set.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)
        # print(request.data)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)        
            return Response(serializer.data)


# 댓글 part
# comment 목록 조회, 생성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comments = review.comment_set.order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 단일 comment 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if not request.user.comment_set.filter(pk=comment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            
    elif request.method == 'DELETE':
        if not request.user.comment_set.filter(pk=comment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        data = {
            'id': comment_pk,
            'delete': f'data {comment_pk} is deleted!!',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_likes(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    if user in review.like_users.all():
        review.like_users.remove(user)
        liked = False
    
    else:
        review.like_users.add(user)
        liked = True
        
    return Response({
        "liked": liked,
        "count": review.like_users.count()
    })