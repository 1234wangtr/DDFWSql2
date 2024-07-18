from django.shortcuts import render, redirect
from .forms import VideoPlaceForm, VideoCulturalForm, VideoHumanisticForm
from CoreApp.models import PlaceLocation, PlaceNatural, PlaceHumanistic

def video_place_create(request):
    if request.method == 'POST':
        form = VideoPlaceForm(request.POST)
        print(f"POST video place")
        if form.is_valid():
            print(f"valid video place")
            form.save()
            return redirect('video_place_success')
    else:
        form = VideoPlaceForm()
    return render(request, 'videoapp/video_place_form.html', {'form': form})

def video_place_success(request):
    return render(request, 'videoapp/success.html', {'message': '在地视频添加成功！'})

def video_home(request):
    return render(request, 'videoapp/video_home.html')

from .forms import VideoCulturalForm
def video_cultural_create(request):
    if request.method == 'POST':
        form = VideoCulturalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_cultural_success')
    else:
        form = VideoCulturalForm()
    return render(request, 'videoapp/video_cultural_form.html', {'form': form})

def video_cultural_success(request):
    return render(request, 'videoapp/success.html', {'message': '物产视频添加成功！'})

from .forms import VideoHumanisticForm
def video_humanistic_create(request):
    if request.method == 'POST':
        form = VideoHumanisticForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_humanistic_success')
    else:
        form = VideoHumanisticForm()
    return render(request, 'videoapp/video_humanistic_form.html', {'form': form})

def video_humanistic_success(request):
    return render(request, 'videoapp/success.html', {'message': '文化视频添加成功！'})


from django.shortcuts import render
from django.db.models import Q
from functools import reduce
from .models import VideoPlace, VideoCultural, VideoHumanistic
from .forms import SearchForm

def search(request):
    form = SearchForm()
    results = []
    query = ''

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('keywords', '')
            keywords = query.split(' ')

            video_place_q_objects = [
                Q(place_location_level1__name__icontains=keyword) |
                Q(place_location_level2__name__icontains=keyword) |
                Q(place_location_level3__name__icontains=keyword) |
                Q(place_natural_level1__name__icontains=keyword) |
                Q(place_natural_level2__name__icontains=keyword) |
                Q(place_natural_level3__name__icontains=keyword) |
                Q(place_humanistic_level1__name__icontains=keyword) |
                Q(place_humanistic_level2__name__icontains=keyword) |
                Q(place_humanistic_level3__name__icontains=keyword) |
                Q(keywords__icontains=keyword) |
                Q(copyright_owner__icontains=keyword) |
                Q(information_address__icontains=keyword) |
                Q(season__icontains=keyword) |
                Q(video_class__icontains=keyword) |
                Q(picture_frame__icontains=keyword) |
                Q(special_name__icontains=keyword) |
                Q(dir_name__icontains=keyword)
                for keyword in keywords
            ]
            video_place_q = reduce(lambda x, y: x & y, video_place_q_objects)
            video_place_results = VideoPlace.objects.filter(video_place_q)

            video_cultural_q_objects = [
                Q(cultural_agri_product_level1__name__icontains=keyword) |
                Q(cultural_agri_product_level2__name__icontains=keyword) |
                Q(cultural_delicacies_level1__name__icontains=keyword) |
                Q(cultural_delicacies_level2__name__icontains=keyword) |
                Q(cultural_processed_product_level1__name__icontains=keyword) |
                Q(cultural_processed_product_level2__name__icontains=keyword) |
                Q(keywords__icontains=keyword) |
                Q(copyright_owner__icontains=keyword) |
                Q(information_address__icontains=keyword) |
                Q(season__icontains=keyword) |
                Q(video_class__icontains=keyword) |
                Q(picture_frame__icontains=keyword) |
                Q(special_name__icontains=keyword) |
                Q(dir_name__icontains=keyword)
                for keyword in keywords
            ]
            video_cultural_q = reduce(lambda x, y: x & y, video_cultural_q_objects)
            video_cultural_results = VideoCultural.objects.filter(video_cultural_q)

            video_humanistic_q_objects = [
                Q(humanistic_category_level1__name__icontains=keyword) |
                Q(humanistic_category_level2__name__icontains=keyword) |
                Q(humanistic_heritage_level1__name__icontains=keyword) |
                Q(humanistic_heritage_level2__name__icontains=keyword) |
                Q(humanistic_topic_level1__name__icontains=keyword) |
                Q(humanistic_topic_level2__name__icontains=keyword) |
                Q(keywords__icontains=keyword) |
                Q(copyright_owner__icontains=keyword) |
                Q(information_address__icontains=keyword) |
                Q(season__icontains=keyword) |
                Q(video_class__icontains=keyword) |
                Q(picture_frame__icontains=keyword) |
                Q(special_name__icontains=keyword) |
                Q(dir_name__icontains=keyword)
                for keyword in keywords
            ]
            video_humanistic_q = reduce(lambda x, y: x & y, video_humanistic_q_objects)
            video_humanistic_results = VideoHumanistic.objects.filter(video_humanistic_q)

            results = [
                {'type': 'VideoPlace', 'data': item} for item in video_place_results
            ] + [
                {'type': 'VideoCultural', 'data': item} for item in video_cultural_results
            ] + [
                {'type': 'VideoHumanistic', 'data': item} for item in video_humanistic_results
            ]

    return render(request, 'videoapp/search.html', {'form': form, 'results': results, 'query': query})


from django.shortcuts import render, get_object_or_404

def video_place_detail(request, pk):
    item = get_object_or_404(VideoPlace, pk=pk)
    return render(request, 'videoapp/video_place_detail.html', {'item': item})

def video_cultural_detail(request, pk):
    item = get_object_or_404(VideoCultural, pk=pk)
    return render(request, 'videoapp/video_cultural_detail.html', {'item': item})

def video_humanistic_detail(request, pk):
    item = get_object_or_404(VideoHumanistic, pk=pk)
    return render(request, 'videoapp/video_humanistic_detail.html', {'item': item})