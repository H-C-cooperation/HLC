from django.urls import path
from . import views

urlpatterns = [
    # actor 정보 조회 (전체, 단일)
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/<int:actor_pk>/', views.actor_detail, name='actor_detail'),
    
    # movie 로드 (관리자만 허용)
    path('movies/load/', views.movie_load),

    # movie 정보 조회 (전체, 단일)
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),

    # movie 찜하기
    path('movies/<int:movie_pk>/like/', views.movie_like, name='movie_like'),
    
    # review CRUD
    path('movies/<int:movie_pk>/reviews/', views.review_list_or_create, name='review_list_or_create'),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail, name='review_detail'),
    
    # review 좋아요
    path('reviews/<int:review_pk>/like/', views.review_like, name='review_like'),

    # genre 좋아요
    path('genres/<str:genre_name>/like/', views.genre_like, name='genre_like'),
    
]
