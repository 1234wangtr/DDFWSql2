from django.urls import path
from .views import *

urlpatterns = [
    path('create/place', video_place_create, name='video_place_create'),


    path('', video_home, name='video_home'),
    path('success/place/', video_place_success, name='video_place_success'),
    #
    path('create/cultural/', video_cultural_create, name='video_cultural_create'),
    path('success/cultural/', video_cultural_success, name='video_cultural_success'),
    #
    path('create/humanistic/', video_humanistic_create, name='video_humanistic_create'),
    path('success/humanistic/', video_humanistic_success, name='video_humanistic_success'),
    #
    path('search/', search, name='search_video'),
    path('place/<int:pk>/', video_place_detail, name='video_place_detail'),
    path('cultural/<int:pk>/', video_cultural_detail, name='video_cultural_detail'),
    path('humanistic/<int:pk>/', video_humanistic_detail, name='video_humanistic_detail'),
]