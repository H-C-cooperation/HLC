from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Actor, Movie, Genre ,Review

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ActorSerializer, ActorDetailSerializer, MovieSerializer, MovieDetailSerializer, ReviewSerializer, ReviewDetailSerializer

# 권한 테스트 용
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

# 다른 파일에 관리할까??
import requests
import json

TMDB_API_KEY = 'd88c87eab4e60d92631748ce1dc8d7f5'

def takeGenre():
    print('Fetching movie genres...')
    genreURL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR'
    
    try:
        genreList = requests.get(genreURL)
        if genreList.status_code == 200:
            genreDatas = genreList.json().get('genres')
            for genreData in genreDatas:
                Genre.objects.get_or_create(
                    id=genreData.get('id'),
                    name=genreData.get('name')
                )
        else:
            print(f"Error fetching genres: {genreList.status_code} - {genreList.text}")
            genreDatas = []
    except (AttributeError, KeyError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        genreDatas = []
    
    if not genreDatas:
        print("No genres found.")
    else:
        print(f"{len(genreDatas)} genres fetched successfully.")

def takeMovie():
    for i in range(1, 5):
        # TMDB API를 사용하여 영화 데이터 (인기) 가져오기
        movieURL = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movieList = requests.get(movieURL)
        resDatas = movieList.json().get('results') 

        for resData in resDatas:
            tmp_id = resData.get('id')
            # CREDITS (배우 + 감독(시간 남으면)) 가져오기
            CREDITS_URL = f"https://api.themoviedb.org/3/movie/{tmp_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
            creditsData = requests.get(CREDITS_URL)

            if resData.get('release_date') == None:
                continue

            # movie는 객체, flag는 생성 되었는지 여부
            movie = Movie.objects.create(
                adult = resData.get('adult'),
                backdrop_path = resData.get('backdrop_path'),
                original_language = resData.get('original_language'),
                overview = resData.get('overview'),
                popularity = resData.get('popularity'),
                poster_path = resData.get('poster_path'),
                release_date = resData.get('release_date'),
                title = resData.get('title'),
                vote_average = resData.get('vote_average'),
                # runtime = 
            )
        
            # 영화배우 추가 파트
            castDatas = creditsData.json().get('cast')
            for j in range(6):
                try:
                    actor_name = castDatas[j].get('name')
                    actor_id = castDatas[j].get('id')
                    profile_path = castDatas[i].get('profile_path')
                    movieactor, chk3 = Actor.objects.get_or_create(
                        id = actor_id,
                        name = actor_name,
                        profile_path = profile_path
                    )
                    movie.actors.add(movieactor)
                except:
                    continue
            
            # 장르 추가 파트
            genreItems = resData.get('genre_ids')
            for genre_pk in genreItems:
                genre = get_object_or_404(Genre, pk=genre_pk)
                movie.genres.add(genre)

# @permission_classes([IsAdminUser])
@api_view(['GET'])
def movie_load(request):
    takeGenre()
    takeMovie()

    return Response({'message':'DB 확인하기'})

# 전체 배우 목록
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializers = ActorSerializer(actors, many=True)

    return Response(serializers.data)

# 단일 배우 정보 제공
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)

# 전체 영화 목록 제공
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many=True)
    
    return Response(serializers.data)

# 단일 영화 목록 제공
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    
    return Response(serializer.data)

# 전체 리뷰 목록 제공
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializers = ReviewSerializer(reviews, many=True)
    
    return Response(serializers.data)

# 단일 리뷰 조회 & 수정 & 삭제
@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    
    # 조회
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    # 삭제
    elif request.method == 'DELETE':
        comment = {
            "message": f'review {review.pk} is deleted'
        }
        review.delete()
        return Response(comment, status=status.HTTP_204_NO_CONTENT)
    # 수정 (완전)
    elif request.method == 'PUT': 
        serializer = ReviewDetailSerializer(instance=review,data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    # 수정 (부분)
    elif request.method == 'PATCH': 
        serializer = ReviewDetailSerializer(review, data=request.data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
# 리뷰 생성
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewDetailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)