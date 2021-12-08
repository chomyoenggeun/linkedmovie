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
    path('moviereviews/<int:moviereview_pk>/comments/', views.moviecomment_create), 
    path('moviereviews/comments/<int:moviecomment_pk>/', views.moviecomment_update_delete),    

    # random
    path('random/', views.random),

    # genre
    path('genre/', views.genre),

    # movie like
    path('<int:movie_id>/likes/', views.movie_likes),
    
]
