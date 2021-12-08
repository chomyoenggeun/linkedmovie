from django.urls import path
from . import views

urlpatterns = [
    # movie
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),


    # review
    path('moviereviews/', views.moviereview_list),    
    path('moviereviews/<int:moviereview_pk>/', views.moviereview_detail_update_delete),
    
    # comment
    path('moviereviews/<int:review_pk>/comments/', views.moviecomment_create), 
    path('moviereviews/comments/<int:comment_pk>/', views.moviecomment_update_delete),    

    # genre
    path('genres/', views.genres),
    path('moviegenres/', views.moviegenres),

    # random
    path('random/', views.random),

    # recommend 1
    # path('recommend/', views.recommend, name="addmovie"),

    # recommend 2
    # path('addmovie/', views.addmovie),

    
]
