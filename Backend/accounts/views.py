from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializers import UserSerializer, UserProfileSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse



# def detail(request, username):
#     User = get_user_model()
#     user = get_object_or_404(User, username=username)
#     genre = Genre.objects.all()
#     context = {
#         'user': user,
#         'genre': genre,
#     }
#     return render(request, 'accounts/detail.html', context)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_profile_image(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if user != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    serializer = UserProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    
    if request.method == 'GET':
        serializer = UserSerializer(person)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        print(request.data)
        
        serializer = UserSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    print(request.user)

    # user = get_object_or_404(get_user_model(), pk=request.data['user_id'])
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
        else:
            person.followers.add(user)
        # person 를 UserProfileSerializer 사용하여 응답
        response_serializer = UserSerializer(person)   

        return Response(response_serializer.data)
    