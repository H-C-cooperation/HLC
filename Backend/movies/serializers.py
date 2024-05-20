from rest_framework import serializers
from .models import Actor, Movie, Review, Genre

# 테스트 시리얼라이즈
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ('title', 'overview',)
        fields = '__all__'
        
# 리뷰 전체 조회할 때 만 사용
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'content', 'rate', 'updated_at',)
        read_only_fields = ('movie', 'user',)
        
class ReviewDetailSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
            
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'like_users',)
        
class MovieDetailSerializer(serializers.ModelSerializer):
    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('id', 'name', )
    actors = ActorNameSerializer(many=True ,read_only=True)
    
    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name', )
    genres = ActorNameSerializer(many=True ,read_only=True)

    
    review_set = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies', )

    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', )
    movies = MovieTitleSerializer(many=True, read_only = True)