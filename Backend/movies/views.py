from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ActorSerializer, ActorDetailSerializer, MovieSerializer, MovieDetailSerializer, ReviewSerializer, ReviewDetailSerializer

# 권한 테스트 용
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

# view 함수에서 사용하는 모델
from .models import Actor, Movie, Genre ,Review
User = get_user_model()

# 다른 파일에 관리할까??
import requests
import json

TMDB_API_KEY = 'd88c87eab4e60d92631748ce1dc8d7f5'
YOUTUBE_API_KEY = 'AIzaSyACxJj878xh9pNgnBhs1yW_Ar7vOd0R7F0'
# AIzaSyA3cQDQWcuogFV6t4oZrFXYR2ZfEOlvkpg
# AIzaSyACxJj878xh9pNgnBhs1yW_Ar7vOd0R7F0
def takeYoutubeUrl(movieTitle):
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'key': YOUTUBE_API_KEY,
        'q': f"{movieTitle} 공식 예고편",
        'type': 'video'
    }
    response = requests.get(url, params=params)
    data = response.json()

    try:
        video_id = data['items'][0]['id']['videoId']
    except (IndexError , KeyError):
        print(f"Error: ", movieTitle)
        video_id = ''

    youtube_url = ''
    if video_id:
        youtube_url = f"https://www.youtube.com/embed/{video_id}"
    return youtube_url

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
    cnt = 0
    for i in range(5, 11):
        # TMDB API를 사용하여 영화 데이터 (인기) 가져오기
        movieURL = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movieList = requests.get(movieURL)
        resDatas = movieList.json().get('results') 

        for resData in resDatas:
            tmp_id = resData.get('id')

            DETAIL_URL = f"https://api.themoviedb.org/3/movie/{tmp_id}?api_key={TMDB_API_KEY}&language=ko-KR"
            detailData = requests.get(DETAIL_URL)
            # CREDITS (배우 + 감독(시간 남으면)) 가져오기
            CREDITS_URL = f"https://api.themoviedb.org/3/movie/{tmp_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
            creditsData = requests.get(CREDITS_URL)
            # creditsData = detailData.get('credits')

            # 예외 처리 : 빈 값이 있을 수 있는 필드는 db에 저장하면 not null 에러가 난다 => 이를 제외하기 
            if resData.get('release_date') == None or detailData.json().get('runtime') == None:
                print(resData.get('release_date'), detailData.json().get('runtime'))
                cnt += 1
                continue
            
            # youtube 공식 예고편 링크 가져오기 (혹시라도 제목 없으면 에러 메시지 띄우기 위해 index 로 사용)
            youtube_url = takeYoutubeUrl(resData['title'])

            # 공식 예고편을 찾을 수 없다면 없애 주기
            if youtube_url == '':
                cnt += 1
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
                vote_count = resData.get('vote_count'),
                runtime = detailData.json().get('runtime'),
                youtube_url = youtube_url,
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

    print(f'{cnt} 개의 영화가 제외됨')

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

# ============================================================================= (고마워 지피티)
# 사용자 기반 협업 필터링
from scipy.stats import pearsonr
from operator import itemgetter

def user_similarity(user1, user2):
    user1_reviews = user1.reviews.values_list('movie_id', 'rate')
    user2_reviews = user2.reviews.values_list('movie_id', 'rate')

    # 두 사용자가 공통으로 평가한 영화 ID 목록 추출
    common_movies = set([m1 for m1, _ in user1_reviews]) & set([m2 for m2, _ in user2_reviews])

    # 공통 영화에 대한 평점 리스트 생성
    user1_rates = [rate for movie_id, rate in user1_reviews if movie_id in common_movies]
    user2_rates = [rate for movie_id, rate in user2_reviews if movie_id in common_movies]

    # 피어슨 상관계수 계산
    return pearsonr(user1_rates, user2_rates)[0]

def get_top_k_similar_users(target_user, k=5):
    # 타겟 사용자와 다른 사용자들의 유사도 계산
    similarities = [(other_user, user_similarity(target_user, other_user)) for other_user in User.objects.exclude(id=target_user.id)]
    
    # 유사도가 높은 순으로 정렬
    similarities.sort(key=itemgetter(1), reverse=True)
    
    # 상위 k명의 유사 사용자 반환
    return [user for user, _ in similarities[:k]]

def get_recommendations(target_user):
    # 타겟 사용자와 유사한 사용자 k명 찾기
    similar_users = get_top_k_similar_users(target_user)
    
    # 타겟 사용자가 아직 보지 않은 영화 목록 추출
    watched_movies = target_user.reviews.values_list('movie_id', flat=True)
    unwatched_movies = Movie.objects.exclude(id__in=watched_movies)
    
    # 유사 사용자들의 평점을 활용하여 추천 점수 계산
    recommendations = []
    for movie in unwatched_movies:
        total_score = 0
        for similar_user in similar_users:
            try:
                similar_user_rating = similar_user.reviews.get(movie=movie).rate
                total_score += similar_user_rating * user_similarity(target_user, similar_user)
            except Review.DoesNotExist:
                pass
        recommendations.append((movie, total_score))
    
    # 추천 점수가 높은 순으로 정렬
    recommendations.sort(key=itemgetter(1), reverse=True)
    
    return [movie for movie, _ in recommendations]

# ===========================================================================

# 전체 영화 목록 제공
@api_view(['GET'])
def movie_list(request):
    # movies = Movie.objects.all()

    mode = request.GET.get('mode')
    
    # 유사한 사용자 추천 알고리즘  <= 조금 더 할 필요가 있어요.
    if mode == 'algorithm':
        target_user_id = request.user.id
        target_user = User.objects.get(id=target_user_id)
        recommendations = get_recommendations(target_user)
        movies = Movie.objects.filter(id__in=[movie.id for movie in recommendations])[:30]
    # 최신순, 평점순, 인기순
    elif mode in ('release_date', 'vote_average', 'popularity'):
        movies = Movie.objects.order_by(f'-{mode}')[:30]

    # 런타임 => TO DO
    elif mode == 'runtime':
        inputRuntime = request.GET.get('inputRuntime')
        if inputRuntime == 'short': # runtime : 0 <= x < 1 시간
            movies = Movie.objects.filter(runtime__gt=0, runtime__lt=90).order_by('-popularity')[:30]
        elif inputRuntime == 'medium': # runtime : 1 <= x < 2 시간
            movies = Movie.objects.filter(runtime__gte=90, runtime__lt=150).order_by('-popularity')[:30]
        elif inputRuntime == 'long': # runtime : 2시간 이상
            movies = Movie.objects.filter(runtime__gte=150).order_by('-popularity')[:30]

    # 장르별 인기순
    elif mode == 'genre':
        inputGenre = request.GET.get('inputGenre')
        genre = Genre.objects.get(name=inputGenre)

        movies = genre.movies.order_by('-popularity')[:30]
    # 디폴트 - 그냥 db에서 가져오기
    else:
        movies = Movie.objects.all()[:2]

    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)

# 단일 영화 목록 제공
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    
    return Response(serializer.data)

# 영화 찜하기
@api_view(['POST'])
def movie_like(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        liked = False
    else:
        movie.like_users.add(user)
        liked =True
    context ={
        'liked' : liked,
        'count' : movie.like_users.count(),
    }

    return Response(context)

from django.db.models import Count
# 해당 영화에 등록된 전체 리뷰 목록 제공 + 리뷰 생성
@api_view(['GET', 'POST'])
def review_list_or_create(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)

    # 리뷰 목록 제공
    if request.method == 'GET':
        mode = request.GET.get('mode')
        if mode == 'date':
            reviews = movie.reviews.order_by('-updated_at')
        else:
            reviews = movie.reviews.annotate(like_count=Count('like_users')).order_by('-like_count')
        serializers = ReviewSerializer(reviews, many=True)
        
        return Response(serializers.data)
    # 리뷰 생성
    elif request.method == 'POST':

        # 현재 사용자가 작성한 리뷰가 영화 리뷰에 있는 경우 => 새로운 리뷰 작성 불가능
        if request.user in [review.user for review in movie.reviews.all()]:
            return Response({'message':'현재 작성된 리뷰가 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReviewDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            review = serializer.save(movie=movie, user=request.user)

            # 영화 평점 업데이트
            movie.vote_average = ((movie.vote_average) * (movie.vote_count) + (review.rate) * 2) / ((movie.vote_count) + 1)
            movie.vote_count += 1
            movie.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 단일 리뷰 조회 & 수정 & 삭제
@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def review_detail(request, movie_pk ,review_pk):
    review = Review.objects.get(pk=review_pk)
    movie = Movie.objects.get(pk=movie_pk)

    # 해당 movie에 달려있는 리뷰가 아니라면 예외 처리
    if review not in movie.reviews.all():
        print('해당 영화에 달린 리뷰가 아닙니다.')
        return Response({'해당 영화에 달린 리뷰가 아닙니다.'})

    # 다른 유저가 수정, 삭제 못하게 예외 처리
    if request.user != review.user:
        print('리뷰 작성자만 수정 및 삭제가 가능합니다.')
        return Response({'message:''리뷰 작성자만 수정 및 삭제가 가능합니다.'})

    # 조회
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    # 삭제
    elif request.method == 'DELETE':
        comment = {
            "message": f'review {review.pk} is deleted'
        }

        print('업뎃 전: ',movie.vote_average)

        # 영화 평점 업데이트
        movie.vote_average = ((movie.vote_average) * (movie.vote_count) - (review.rate) * 2) / ((movie.vote_count) - 1)
        movie.vote_count -= 1
        movie.save()

        print('업댓 후: ',movie.vote_average)
        
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

# 리뷰 좋아요
@api_view(['POST'])
def review_like(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)

    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        liked = False
    else:
        review.like_users.add(user)
        liked =True
    context ={
        'liked' : liked,
        'count' : review.like_users.count(),
    }

    return Response(context)

# 장르 좋아요
@api_view(['POST'])
def genre_like(request, genre_name):
    user = request.user
    genre = get_object_or_404(Genre, name=genre_name)

    if genre.like_users.filter(pk=user.pk).exists():
        genre.like_users.remove(user)
        liked = False
    else:
        genre.like_users.add(user)
        liked =True
    context ={
        'liked' : liked,
        'count' : genre.like_users.count(),
    }

    return Response(context)