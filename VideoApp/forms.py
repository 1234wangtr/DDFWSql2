from django import forms
from .models import *
from CoreApp.models import *

class VideoPlaceForm(forms.ModelForm):
    class Meta:
        model = VideoPlace
        fields = [
            'keywords', 'information_address', 'copyright_owner',
            'dir_name', 'special_name', 'season', 'video_class', 'picture_frame',
            'place_location_level1', 'place_location_level2', 'place_location_level3',
            'place_natural_level1', 'place_natural_level2', 'place_natural_level3',
            'place_humanistic_level1', 'place_humanistic_level2', 'place_humanistic_level3',
        ]

        widgets = {
            'place_location_level1': forms.Select(attrs={'class': 'place_location_level1'}),
            'place_location_level2': forms.Select(attrs={'class': 'place_location_level2'}),
            'place_location_level3': forms.Select(attrs={'class': 'place_location_level3'}),
            'place_natural_level1': forms.Select(attrs={'class': 'place_natural_level1'}),
            'place_natural_level2': forms.Select(attrs={'class': 'place_natural_level2'}),
            'place_natural_level3': forms.Select(attrs={'class': 'place_natural_level3'}),
            'place_humanistic_level1': forms.Select(attrs={'class': 'place_humanistic_level1'}),
            'place_humanistic_level2': forms.Select(attrs={'class': 'place_humanistic_level2'}),
            'place_humanistic_level3': forms.Select(attrs={'class': 'place_humanistic_level3'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['place_location_level1'].queryset = PlaceLocation.objects.filter(parent__isnull=True)

        self.fields['place_natural_level1'].queryset = PlaceNatural.objects.filter(parent__isnull=True)

        self.fields['place_humanistic_level1'].queryset = PlaceHumanistic.objects.filter(parent__isnull=True)


        if 'place_location_level1' in self.data:
            try:
                parent_id = int(self.data.get('place_location_level1'))
                self.fields['place_location_level2'].queryset = PlaceLocation.objects.filter(parent_id=parent_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['place_location_level2'].queryset = PlaceLocation.objects.none()
        else:
            self.fields['place_location_level2'].queryset = PlaceLocation.objects.none()

        if 'place_location_level2' in self.data:
            try:
                parent_id = int(self.data.get('place_location_level2'))
                self.fields['place_location_level3'].queryset = PlaceLocation.objects.filter(parent_id=parent_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['place_location_level3'].queryset = PlaceLocation.objects.none()
        else:
            self.fields['place_location_level3'].queryset = PlaceLocation.objects.none()

        if 'place_natural_level1' in self.data:
            try:
                parent_id = int(self.data.get('place_natural_level1'))
                self.fields['place_natural_level2'].queryset = PlaceNatural.objects.filter(parent_id=parent_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['place_natural_level2'].queryset = PlaceNatural.objects.none()
        else:
            self.fields['place_natural_level2'].queryset = PlaceNatural.objects.none()

        if 'place_natural_level2' in self.data:
            try:
                parent_id = int(self.data.get('place_natural_level2'))
                self.fields['place_natural_level3'].queryset = PlaceNatural.objects.filter(parent_id=parent_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['place_natural_level3'].queryset = PlaceNatural.objects.none()
        else:
            self.fields['place_natural_level3'].queryset = PlaceNatural.objects.none()

        if 'place_humanistic_level1' in self.data:
            try:
                parent_id = int(self.data.get('place_humanistic_level1'))
                self.fields['place_humanistic_level2'].queryset = PlaceHumanistic.objects.filter(parent_id=parent_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['place_humanistic_level2'].queryset = PlaceHumanistic.objects.none()
        else:
            self.fields['place_humanistic_level2'].queryset = PlaceHumanistic.objects.none()

        if 'place_humanistic_level2' in self.data:
            try:
                parent_id = int(self.data.get('place_humanistic_level2'))
                self.fields['place_humanistic_level3'].queryset = PlaceHumanistic.objects.filter(parent_id=parent_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['place_humanistic_level3'].queryset = PlaceHumanistic.objects.none()
        else:
            self.fields['place_humanistic_level3'].queryset = PlaceHumanistic.objects.none()

class VideoCulturalForm(forms.ModelForm):
    class Meta:
        model = VideoCultural
        fields = [
            'keywords', 'information_address', 'copyright_owner',
            'dir_name', 'special_name', 'season', 'video_class', 'picture_frame',
            'cultural_agri_product_level1', 'cultural_agri_product_level2',
            'cultural_delicacies_level1', 'cultural_delicacies_level2',
            'cultural_processed_product_level1', 'cultural_processed_product_level2'
        ]

        widgets = {
            'cultural_agri_product_level1': forms.Select(attrs={'class': 'cultural_agri_product_level1'}),
            'cultural_agri_product_level2': forms.Select(attrs={'class': 'cultural_agri_product_level2'}),
            'cultural_delicacies_level1': forms.Select(attrs={'class': 'cultural_delicacies_level1'}),
            'cultural_delicacies_level2': forms.Select(attrs={'class': 'cultural_delicacies_level2'}),
            'cultural_processed_product_level1': forms.Select(attrs={'class': 'cultural_processed_product_level1'}),
            'cultural_processed_product_level2': forms.Select(attrs={'class': 'cultural_processed_product_level2'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize queryset for cultural_agri_product_level1, cultural_agri_product_level2, etc.
        self.fields['cultural_agri_product_level1'].queryset = CulturalAgriProduct.objects.filter(parent__isnull=True)
        self.fields['cultural_delicacies_level1'].queryset = CulturalDelicacies.objects.filter(parent__isnull=True)
        self.fields['cultural_processed_product_level1'].queryset = CulturalProcessedProduct.objects.filter(parent__isnull=True)


### VideoHumanisticForm

class VideoHumanisticForm(forms.ModelForm):
    class Meta:
        model = VideoHumanistic
        fields = [
            'keywords', 'information_address', 'copyright_owner',
            'dir_name', 'special_name', 'season', 'video_class', 'picture_frame',
            'humanistic_category_level1', 'humanistic_category_level2',
            'humanistic_heritage_level1', 'humanistic_heritage_level2',
            'humanistic_topic_level1', 'humanistic_topic_level2'
        ]

        widgets = {
            'humanistic_category_level1': forms.Select(attrs={'class': 'humanistic_category_level1'}),
            'humanistic_category_level2': forms.Select(attrs={'class': 'humanistic_category_level2'}),
            'humanistic_heritage_level1': forms.Select(attrs={'class': 'humanistic_heritage_level1'}),
            'humanistic_heritage_level2': forms.Select(attrs={'class': 'humanistic_heritage_level2'}),
            'humanistic_topic_level1': forms.Select(attrs={'class': 'humanistic_topic_level1'}),
            'humanistic_topic_level2': forms.Select(attrs={'class': 'humanistic_topic_level2'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize queryset for humanistic_category_level1, humanistic_category_level2, etc.
        self.fields['humanistic_category_level1'].queryset = HumanisticCategory.objects.filter(parent__isnull=True)
        self.fields['humanistic_heritage_level1'].queryset = HumanisticHeritage.objects.filter(parent__isnull=True)
        self.fields['humanistic_topic_level1'].queryset = HumanisticTopic.objects.filter(parent__isnull=True)



class SearchForm(forms.Form):
    keywords = forms.CharField(max_length=255, help_text="输入关键词（用空格分隔）", label='关键词')