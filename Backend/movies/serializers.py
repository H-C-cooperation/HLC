from rest_framework import serializers
from .models import Actor, Movie, Review

# 테스트 시리얼라이즈
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ('title', 'overview',)
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content', )
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
        read_only_fields = ('movie',)
        
class MovieDetailSerializer(serializers.ModelSerializer):
    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name', )
    actor = ActorNameSerializer(read_only=True)
    
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