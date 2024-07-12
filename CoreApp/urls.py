from django.urls import path
from .views import *

urlpatterns = [
    path('get_location_level2/<int:parent_id>/', get_location_level2, name='get_location_level2'),
    path('get_location_level3/<int:parent_id>/', get_location_level3, name='get_location_level3'),
    path('get_natural_level2/<int:parent_id>/', get_natural_level2, name='get_natural_level2'),
    path('get_natural_level3/<int:parent_id>/', get_natural_level3, name='get_natural_level3'),
    path('get_humanistic_level2/<int:parent_id>/', get_humanistic_level2, name='get_humanistic_level2'),
    path('get_humanistic_level3/<int:parent_id>/', get_humanistic_level3, name='get_humanistic_level3'),

    # Repeat similar paths for place_natural and place_humanistic

    # 风物
    path('get_agri_product_level2/<int:parent_id>/', get_agri_product_level2, name='get_agri_product_level2'),
    path('get_delicacies_level2/<int:parent_id>/', get_delicacies_level2, name='get_delicacies_level2'),
    path('get_processed_product_level2/<int:parent_id>/', get_processed_product_level2, name='get_processed_product_level2'),

    # 人文
    path('get_humanistic_category_level2/<int:parent_id>/', get_humanistic_category_level2, name='get_humanistic_category_level2'),
    path('get_humanistic_heritage_level2/<int:parent_id>/', get_humanistic_heritage_level2, name='get_humanistic_heritage_level2'),
    path('get_humanistic_topic_level2/<int:parent_id>/', get_humanistic_topic_level2, name='get_humanistic_topic_level2'),


]
