from rest_framework import serializers
from .models import Actor, Movie, Review, Genre
from accounts.serializers import UserProfileSerializer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ('title', 'overview',)
        fields = '__all__'
        
# 단일 영화 리뷰 전체 조회할 때 사용
class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    formatted_updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'content', 'rate', 'updated_at','formatted_updated_at', 'user', 'like_users')
        read_only_fields = ('movie', 'user', 'like_users')

    def get_formatted_updated_at(self, obj):
        # 원하는 포맷으로 날짜를 변환합니다.
        return obj.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        
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
    
    actors = serializers.SerializerMethodField()
    def get_actors(self, instance):
        class ActorNameSerializer(serializers.ModelSerializer):
            class Meta:
                model = Actor
                fields = ('id', 'name', 'popularity',)
                
        serializer = ActorNameSerializer(instance.actors.order_by('-popularity'), many=True, read_only=True)
        return serializer.data
    
    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name', )
    genres = GenreNameSerializer(many=True ,read_only=True)

    reviews = ReviewSerializer(many=True, read_only=True)
    
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