from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'followers','followings','like_movies', 'like_reviews', 'like_genres',)


# class SignupSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('username', 'nickname',)
        