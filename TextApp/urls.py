from django.urls import path
from .views import *

urlpatterns = [
    path('create/place', text_place_create, name='text_place_create'),
    path('', text_home, name='text_home'),
    path('success/place/', text_place_success, name='text_place_success'),

    path('create/cultural/', text_cultural_create, name='text_cultural_create'),
    path('success/cultural/', text_cultural_success, name='text_cultural_success'),

    path('create/humanistic/', text_humanistic_create, name='text_humanistic_create'),
    path('success/humanistic/', text_humanistic_success, name='text_humanistic_success'),

    path('search/', search, name='search_text'),
    path('place/<int:pk>/', text_place_detail, name='text_place_detail'),
    path('cultural/<int:pk>/', text_cultural_detail, name='text_cultural_detail'),
    path('humanistic/<int:pk>/', text_humanistic_detail, name='text_humanistic_detail'),
]
