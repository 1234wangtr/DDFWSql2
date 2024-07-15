from django import forms
from .models import TextPlace
from CoreApp.models import PlaceLocation, PlaceNatural, PlaceHumanistic

class TextPlaceForm(forms.ModelForm):
    class Meta:
        model = TextPlace
        fields = [
            'keywords', 'information_source', 'information_address', 'copyright_owner',
            'place_location_level1', 'place_location_level2', 'place_location_level3',
            'place_natural_level1', 'place_natural_level2', 'place_natural_level3',
            'place_humanistic_level1', 'place_humanistic_level2', 'place_humanistic_level3'
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
        super(TextPlaceForm, self).__init__(*args, **kwargs)
        self.fields['place_location_level1'].queryset = PlaceLocation.objects.filter(parent__isnull=True)
        self.fields['place_natural_level1'].queryset = PlaceNatural.objects.filter(parent__isnull=True)
        self.fields['place_humanistic_level1'].queryset = PlaceHumanistic.objects.filter(parent__isnull=True)

    # clean似乎没用
    def clean(self):
        cleaned_data = super().clean()

        # Clean place_location levels
        place_location_level1 = cleaned_data.get('place_location_level1')
        place_location_level2 = cleaned_data.get('place_location_level2')
        place_location_level3 = cleaned_data.get('place_location_level3')

        if not place_location_level1:
            cleaned_data['place_location_level2'] = None
            cleaned_data['place_location_level3'] = None
        elif not place_location_level2:
            cleaned_data['place_location_level3'] = None

        # Clean place_natural levels
        place_natural_level1 = cleaned_data.get('place_natural_level1')
        place_natural_level2 = cleaned_data.get('place_natural_level2')
        place_natural_level3 = cleaned_data.get('place_natural_level3')

        if not place_natural_level1:
            cleaned_data['place_natural_level2'] = None
            cleaned_data['place_natural_level3'] = None
        elif not place_natural_level2:
            cleaned_data['place_natural_level3'] = None

        # Clean place_humanistic levels
        place_humanistic_level1 = cleaned_data.get('place_humanistic_level1')
        place_humanistic_level2 = cleaned_data.get('place_humanistic_level2')
        place_humanistic_level3 = cleaned_data.get('place_humanistic_level3')

        if not place_humanistic_level1:
            cleaned_data['place_humanistic_level2'] = None
            cleaned_data['place_humanistic_level3'] = None
        elif not place_humanistic_level2:
            cleaned_data['place_humanistic_level3'] = None

        return cleaned_data



from django import forms
from .models import TextCultural
from CoreApp.models import CulturalAgriProduct, CulturalDelicacies, CulturalProcessedProduct

class TextCulturalForm(forms.ModelForm):
    class Meta:
        model = TextCultural
        fields = [
            'keywords', 'information_source', 'information_address', 'copyright_owner',
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
        super(TextCulturalForm, self).__init__(*args, **kwargs)
        self.fields['cultural_agri_product_level1'].queryset = CulturalAgriProduct.objects.filter(parent__isnull=True)
        self.fields['cultural_delicacies_level1'].queryset = CulturalDelicacies.objects.filter(parent__isnull=True)
        self.fields['cultural_processed_product_level1'].queryset = CulturalProcessedProduct.objects.filter(parent__isnull=True)

    # clean似乎没用
    def clean(self):
        cleaned_data = super().clean()

        # Clean cultural_agri_product levels
        cultural_agri_product_level1 = cleaned_data.get('cultural_agri_product_level1')
        cultural_agri_product_level2 = cleaned_data.get('cultural_agri_product_level2')

        if not cultural_agri_product_level1:
            cleaned_data['cultural_agri_product_level2'] = None

        # Clean cultural_delicacies levels
        cultural_delicacies_level1 = cleaned_data.get('cultural_delicacies_level1')
        cultural_delicacies_level2 = cleaned_data.get('cultural_delicacies_level2')

        if not cultural_delicacies_level1:
            cleaned_data['cultural_delicacies_level2'] = None

        # Clean cultural_processed_product levels
        cultural_processed_product_level1 = cleaned_data.get('cultural_processed_product_level1')
        cultural_processed_product_level2 = cleaned_data.get('cultural_processed_product_level2')

        if not cultural_processed_product_level1:
            cleaned_data['cultural_processed_product_level2'] = None

        return cleaned_data



from django import forms
from .models import TextHumanistic
from CoreApp.models import HumanisticTopic, HumanisticCategory, HumanisticHeritage

class TextHumanisticForm(forms.ModelForm):
    class Meta:
        model = TextHumanistic
        fields = [
            'keywords', 'information_source', 'information_address', 'copyright_owner',
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
        super(TextHumanisticForm, self).__init__(*args, **kwargs)
        self.fields['humanistic_category_level1'].queryset = HumanisticCategory.objects.filter(parent__isnull=True)
        self.fields['humanistic_heritage_level1'].queryset = HumanisticHeritage.objects.filter(parent__isnull=True)
        self.fields['humanistic_topic_level1'].queryset = HumanisticTopic.objects.filter(parent__isnull=True)


# 搜索
from django import forms

class SearchForm(forms.Form):
    keywords = forms.CharField(max_length=255, help_text="输入关键词（用空格分隔）", label='关键词')

