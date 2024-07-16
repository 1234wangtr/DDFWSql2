from django.urls import path
from .views import *

urlpatterns = [
    path('create/place', img_place_create, name='img_place_create'),


    path('', img_home, name='img_home'),
    path('success/place/', img_place_success, name='img_place_success'),
    #
    path('create/cultural/', img_cultural_create, name='img_cultural_create'),
    path('success/cultural/', img_cultural_success, name='img_cultural_success'),
    #
    path('create/humanistic/', img_humanistic_create, name='img_humanistic_create'),
    path('success/humanistic/', img_humanistic_success, name='img_humanistic_success'),
    #
    path('search/', search, name='search_img'),
    path('place/<int:pk>/', img_place_detail, name='img_place_detail'),
    path('cultural/<int:pk>/', img_cultural_detail, name='img_cultural_detail'),
    path('humanistic/<int:pk>/', img_humanistic_detail, name='img_humanistic_detail'),
]
