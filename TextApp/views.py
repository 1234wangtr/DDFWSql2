from django.shortcuts import render, redirect
from .forms import *

def text_place_create(request):
    if request.method == 'POST':
        form = TextPlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('text_place_success')
    else:
        form = TextPlaceForm()
    return render(request, 'textapp/text_place_form.html', {'form': form})

def text_place_success(request):
    #return render(request, 'textapp/text_place_success.html')
    return render(request, 'textapp/success.html', {'message': 'TextPlace created successfully!'})

def text_home(request):
    return render(request, 'textapp/text_home.html')


def text_cultural_create(request):
    if request.method == 'POST':
        form = TextCulturalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('text_cultural_success')
    else:
        form = TextCulturalForm()
    return render(request, 'textapp/text_cultural_form.html', {'form': form})

def text_cultural_success(request):
    return render(request, 'textapp/success.html', {'message': 'TextCultural created successfully!'})


from django.shortcuts import render, redirect
from .forms import TextHumanisticForm

def text_humanistic_create(request):
    if request.method == 'POST':
        form = TextHumanisticForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('text_humanistic_success')
    else:
        form = TextHumanisticForm()
    return render(request, 'textapp/text_humanistic_form.html', {'form': form})

def text_humanistic_success(request):
    return render(request, 'textapp/success.html', {'message': 'TextHumanistic created successfully!'})

# 搜索
from django.db.models import Q

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
            print(keywords)
            # Process TextPlace filtering
            text_place_q_objects = [Q(
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
            text_place_q = reduce(and_, text_place_q_objects)

            text_place_results = TextPlace.objects.filter(text_place_q)

            text_cultural_q_objects = [Q(
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

            text_cultural_q = reduce(and_, text_cultural_q_objects)

            text_cultural_results = TextCultural.objects.filter(text_cultural_q)

            text_humanistic_q_objects = [Q(
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

            text_humanistic_q = reduce(and_, text_humanistic_q_objects)

            text_humanistic_results = TextHumanistic.objects.filter(text_humanistic_q)




            results = [
                {'type': 'TextPlace', 'data': item} for item in text_place_results
            ] + [
                {'type': 'TextCultural', 'data': item} for item in text_cultural_results
            ] + [
                {'type': 'TextHumanistic', 'data': item} for item in text_humanistic_results
            ]

    return render(request, 'textapp/search.html', {'form': form, 'results': results, 'query': query})



from django.shortcuts import render, get_object_or_404

def text_place_detail(request, pk):
    item = get_object_or_404(TextPlace, pk=pk)
    return render(request, 'textapp/text_place_detail.html', {'item': item})

def text_cultural_detail(request, pk):
    item = get_object_or_404(TextCultural, pk=pk)
    return render(request, 'textapp/text_cultural_detail.html', {'item': item})

def text_humanistic_detail(request, pk):
    item = get_object_or_404(TextHumanistic, pk=pk)
    return render(request, 'textapp/text_humanistic_detail.html', {'item': item})





