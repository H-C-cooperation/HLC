from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:user_pk>/', views.profile),
    path('<int:user_pk>/follow/', views.follow),
    path('profile/<int:user_pk>/upload_image/', views.upload_profile_image, name='upload_image'),
]


