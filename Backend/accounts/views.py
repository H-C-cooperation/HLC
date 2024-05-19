from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
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


@api_view(['GET'])
def profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = UserSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    print(request.user)

    # user = get_object_or_404(get_user_model(), pk=request.data['user_id'])
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            is_followed = False
        else:
            person.followers.add(user)
            is_followed = True
        return Response(is_followed)