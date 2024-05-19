from django.db import models
from django.conf import settings

# Create your models here.
# 테스트 모델
class Movie(models.Model):
    # 영화배우와 장르는 N:M 연결
    actors = models.ManyToManyField("Actor", related_name='movies')
    genres = models.ManyToManyField("Genre", related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)

    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=100)
    original_language = models.CharField(max_length=10)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    title = models.CharField(max_length=50)
    vote_average = models.FloatField()

    # 런타임
    # runtime = models.IntegerField()
    
    def __str__(self):
        return self.title


class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=150)
    def __str__ (self):
        return self.name

class Genre(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres', blank=True)
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    def __str__ (self):
        return self.name
    
class Review(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  

    title = models.CharField(max_length=100)
    rate = models.FloatField() # 평점
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)