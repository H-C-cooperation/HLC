from rest_framework import serializers
from .models import User
from movies.models import Movie, Review, Genre

class UserProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'image', )

class UserSerializer(serializers.ModelSerializer):
    class MovieProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'youtube_url', )
    
    class ReviewProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('id', 'rate', 'content' )
    
    class GenreProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name', )

    # class UserProfileSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = User
    #         fields = ('username', 'image', )

    like_movies = MovieProfileSerializer(many=True, read_only=True)
    reviews = ReviewProfileSerializer(many=True, read_only=True)
    like_reviews = ReviewProfileSerializer(many=True, read_only=True)
    like_genres = GenreProfileSerializer(many=True, read_only=True)
    followers = UserProfileSerializer(many=True, read_only=True)
    followings = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'followers','followings','like_movies', 'like_reviews', 'reviews', 'like_genres', 'image')
    

# class SignupSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('username', 'nickname',)
        