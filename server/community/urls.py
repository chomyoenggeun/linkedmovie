from django.urls import path
from . import views

# app_name = ''

urlpatterns = [
    #GET: 전체글조회, POST: 게시글 생성
    path('', views.review_list),
    #GET: 단일 게시글 조회, DELETE: 해당 게시글 삭제, PUT: 해당 게시글 수정
    path('<int:review_pk>/', views.review_update_delete),

    
    #GET: 댓글 전체를 조회
    path('<int:review_pk>/comments/', views.comment_create),
    #GET: 단일 댓글 조회, PUT: 댓글 수정, DELETE: 댓글 삭제
    path('comments/<int:comment_pk>/', views.comment_update_delete),

    ######################################################

    # 리뷰 좋아요
    path('<int:review_pk>/likes/', views.review_likes),
]
