from django.shortcuts import render

# Create your views here.

# 主页

def core_home(request):
    return render(request, 'coreapp/core_home.html')


# 在地
from django.http import JsonResponse
from .models import PlaceLocation, PlaceNatural, PlaceHumanistic

def get_location_level2(request, parent_id):
    options = PlaceLocation.objects.filter(parent_id=parent_id).values('id', 'name')
    data = {option['id']: option['name'] for option in options}
    return JsonResponse(data)

def get_location_level3(request, parent_id):
    options = PlaceLocation.objects.filter(parent_id=parent_id).values('id', 'name')
    data = {option['id']: option['name'] for option in options}
    return JsonResponse(data)

# Repeat similar views for place_natural and place_humanistic

def get_natural_level2(request, parent_id):
    options = PlaceNatural.objects.filter(parent_id=parent_id).values('id', 'name')
    data = {option['id']: option['name'] for option in options}
    return JsonResponse(data)

def get_natural_level3(request, parent_id):
    options = PlaceNatural.objects.filter(parent_id=parent_id).values('id', 'name')
    data = {option['id']: option['name'] for option in options}
    return JsonResponse(data)

def get_humanistic_level2(request, parent_id):
    options = PlaceHumanistic.objects.filter(parent_id=parent_id).values('id', 'name')
    data = {option['id']: option['name'] for option in options}
    return JsonResponse(data)

def get_humanistic_level3(request, parent_id):
    options = PlaceHumanistic.objects.filter(parent_id=parent_id).values('id', 'name')
    data = {option['id']: option['name'] for option in options}
    return JsonResponse(data)



# 风物

from django.http import JsonResponse
from .models import CulturalAgriProduct, CulturalDelicacies, CulturalProcessedProduct

def get_agri_product_level2(request, parent_id):
    try:
        level2_items = CulturalAgriProduct.objects.filter(parent_id=parent_id)
        data = {item.id: item.name for item in level2_items}
        return JsonResponse(data)
    except CulturalAgriProduct.DoesNotExist:
        return JsonResponse({})

def get_delicacies_level2(request, parent_id):
    try:
        level2_items = CulturalDelicacies.objects.filter(parent_id=parent_id)
        data = {item.id: item.name for item in level2_items}
        return JsonResponse(data)
    except CulturalDelicacies.DoesNotExist:
        return JsonResponse({})

def get_processed_product_level2(request, parent_id):
    try:
        level2_items = CulturalProcessedProduct.objects.filter(parent_id=parent_id)
        data = {item.id: item.name for item in level2_items}
        return JsonResponse(data)
    except CulturalProcessedProduct.DoesNotExist:
        return JsonResponse({})


# 人文
from django.http import JsonResponse
from .models import HumanisticCategory, HumanisticHeritage, HumanisticTopic

def get_humanistic_category_level2(request, parent_id):
    level2_items = HumanisticCategory.objects.filter(parent_id=parent_id)
    data = {item.id: item.name for item in level2_items}
    return JsonResponse(data)

def get_humanistic_heritage_level2(request, parent_id):
    level2_items = HumanisticHeritage.objects.filter(parent_id=parent_id)
    data = {item.id: item.name for item in level2_items}
    return JsonResponse(data)

def get_humanistic_topic_level2(request, parent_id):
    level2_items = HumanisticTopic.objects.filter(parent_id=parent_id)
    data = {item.id: item.name for item in level2_items}
    return JsonResponse(data)






