# ImgApp/views.py
from django.shortcuts import render, redirect
from .forms import ImgPlaceForm
from CoreApp.models import PlaceLocation, PlaceNatural, PlaceHumanistic

def img_place_create(request):
    if request.method == 'POST':
        form = ImgPlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('img_place_success')
    else:
        form = ImgPlaceForm()
    return render(request, 'imgapp/img_place_form.html', {'form': form})

def img_place_success(request):
    return render(request, 'imgapp/success.html', {'message': 'ImgPlace created successfully!'})

def img_home(request):
    return render(request, 'imgapp/img_home.html')

from .forms import ImgCulturalForm
def img_cultural_create(request):
    if request.method == 'POST':
        form = ImgCulturalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('img_cultural_success')
    else:
        form = ImgCulturalForm()
    return render(request, 'imgapp/img_cultural_form.html', {'form': form})

def img_cultural_success(request):
    return render(request, 'imgapp/success.html', {'message': 'ImgCultural created successfully!'})

from .forms import ImgHumanisticForm
def img_humanistic_create(request):
    if request.method == 'POST':
        form = ImgHumanisticForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('img_humanistic_success')
    else:
        form = ImgHumanisticForm()
    return render(request, 'imgapp/img_humanistic_form.html', {'form': form})

def img_humanistic_success(request):
    return render(request, 'imgapp/success.html', {'message': 'ImgHumanistic created successfully!'})




from .forms import SearchForm
from django.db.models import Q
from .models import *

from functools import reduce
from operator import and_

def search(request):
    form = SearchForm()
    results = []
    query = ''

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('keywords', '')
            keywords = query.split(' ')

            img_place_q_objects = [Q(
                place_location_level1__name__icontains=keyword) |
                                    Q(place_location_level2__name__icontains=keyword) |
                                    Q(place_location_level3__name__icontains=keyword) |
                                    Q(place_natural_level1__name__icontains=keyword) |
                                    Q(place_natural_level2__name__icontains=keyword) |
                                    Q(place_natural_level3__name__icontains=keyword) |
                                    Q(place_humanistic_level1__name__icontains=keyword) |
                                    Q(place_humanistic_level2__name__icontains=keyword) |
                                    Q(place_humanistic_level3__name__icontains=keyword) |
                                    Q(keywords__icontains=keyword) |
                                    Q(information_source__icontains=keyword) |
                                    Q(copyright_owner__icontains=keyword) |
                                    Q(information_address__icontains=keyword)
                                    for keyword in keywords
                                    ]
            # print(f"text place q objcets:{text_place_q_objects}")
            img_place_q = reduce(and_, img_place_q_objects)

            img_place_results = ImgPlace.objects.filter(img_place_q)

            img_cultural_q_objects = [Q(
                cultural_agri_product_level1__name__icontains=keyword) |
                                       Q(cultural_agri_product_level2__name__icontains=keyword) |
                                       Q(cultural_delicacies_level1__name__icontains=keyword) |
                                       Q(cultural_delicacies_level2__name__icontains=keyword) |
                                       Q(cultural_processed_product_level1__name__icontains=keyword) |
                                       Q(cultural_processed_product_level2__name__icontains=keyword) |
                                       Q(keywords__icontains=keyword) |
                                       Q(information_source__icontains=keyword) |
                                       Q(copyright_owner__icontains=keyword) |
                                       Q(information_address__icontains=keyword)
                                       for keyword in keywords
                                       ]

            img_cultural_q = reduce(and_, img_cultural_q_objects)

            img_cultural_results = ImgCultural.objects.filter(img_cultural_q)

            img_humanistic_q_objects = [Q(
                humanistic_category_level1__name__icontains=keyword) |
                                         Q(humanistic_category_level2__name__icontains=keyword) |
                                         Q(humanistic_heritage_level1__name__icontains=keyword) |
                                         Q(humanistic_heritage_level2__name__icontains=keyword) |
                                         Q(humanistic_topic_level1__name__icontains=keyword) |
                                         Q(humanistic_topic_level2__name__icontains=keyword) |
                                         Q(keywords__icontains=keyword) |
                                         Q(information_source__icontains=keyword) |
                                         Q(copyright_owner__icontains=keyword) |
                                         Q(information_address__icontains=keyword)
                                         for keyword in keywords
                                         ]

            img_humanistic_q = reduce(and_, img_humanistic_q_objects)

            img_humanistic_results = ImgHumanistic.objects.filter(img_humanistic_q)

            results = [
                {'type': 'ImgPlace', 'data': item} for item in img_place_results
            ] + [
                {'type': 'ImgCultural', 'data': item} for item in img_cultural_results
            ] + [
                {'type': 'ImgHumanistic', 'data': item} for item in img_humanistic_results
            ]

    return render(request, 'imgapp/search.html', {'form': form, 'results': results, 'query': query})



from django.shortcuts import render, get_object_or_404

def img_place_detail(request, pk):
    item = get_object_or_404(ImgPlace, pk=pk)
    return render(request, 'imgapp/img_place_detail.html', {'item': item})

def img_cultural_detail(request, pk):
    item = get_object_or_404(ImgCultural, pk=pk)
    return render(request, 'imgapp/img_cultural_detail.html', {'item': item})

def img_humanistic_detail(request, pk):
    item = get_object_or_404(ImgHumanistic, pk=pk)
    return render(request, 'imgapp/img_humanistic_detail.html', {'item': item})