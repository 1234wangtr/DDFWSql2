from django.db import models
from CoreApp.models import (
    PlaceLocation, PlaceNatural, PlaceHumanistic,
    CulturalAgriProduct, CulturalDelicacies, CulturalProcessedProduct,
    HumanisticCategory, HumanisticHeritage, HumanisticTopic
)

SOURCE_CHOICES = [
    ('地道风物', '地道风物'),
    ('图书', '图书'),
    ('专家', '专家'),
    ('网络', '网络')
]


COPYRIGHT_CHOICES = [
    ('自有', '自有'),
    ('共有', '共有'),
    ('他人', '他人'),
]

class TextPlace(models.Model):
    keywords = models.TextField(blank=True, null=True)
    information_source = models.CharField(max_length=20, choices=SOURCE_CHOICES, blank=True, null=True)
    information_address = models.TextField(blank=True, null=True)
    copyright_owner = models.CharField(max_length=10, choices=COPYRIGHT_CHOICES, default='自有')

    place_location_level1 = models.ForeignKey(PlaceLocation, on_delete=models.CASCADE,
                                              related_name='text_places_location_level1', blank=True, null=True)
    place_location_level2 = models.ForeignKey(PlaceLocation, on_delete=models.CASCADE,
                                              related_name='text_places_location_level2', blank=True, null=True)
    place_location_level3 = models.ForeignKey(PlaceLocation, on_delete=models.CASCADE,
                                              related_name='text_places_location_level3', blank=True, null=True)

    place_natural_level1 = models.ForeignKey(PlaceNatural, on_delete=models.CASCADE,
                                             related_name='text_places_natural_level1', blank=True, null=True)
    place_natural_level2 = models.ForeignKey(PlaceNatural, on_delete=models.CASCADE,
                                             related_name='text_places_natural_level2', blank=True, null=True)
    place_natural_level3 = models.ForeignKey(PlaceNatural, on_delete=models.CASCADE,
                                             related_name='text_places_natural_level3', blank=True, null=True)

    place_humanistic_level1 = models.ForeignKey(PlaceHumanistic, on_delete=models.CASCADE,
                                                related_name='text_places_humanistic_level1', blank=True, null=True)
    place_humanistic_level2 = models.ForeignKey(PlaceHumanistic, on_delete=models.CASCADE,
                                                related_name='text_places_humanistic_level2', blank=True, null=True)
    place_humanistic_level3 = models.ForeignKey(PlaceHumanistic, on_delete=models.CASCADE,
                                                related_name='text_places_humanistic_level3', blank=True, null=True)

    def __str__(self):
        return f"TextPlace: {self.keywords}"


class TextCultural(models.Model):
    keywords = models.TextField(blank=True, null=True)
    information_source = models.CharField(max_length=20, choices=SOURCE_CHOICES, blank=True, null=True)
    information_address = models.TextField(blank=True, null=True)
    copyright_owner = models.CharField(max_length=10, choices=COPYRIGHT_CHOICES, default='自有')

    cultural_agri_product_level1 = models.ForeignKey(CulturalAgriProduct, on_delete=models.CASCADE,
                                                     related_name='text_culturals_agri_product_level1', blank=True,
                                                     null=True)
    cultural_agri_product_level2 = models.ForeignKey(CulturalAgriProduct, on_delete=models.CASCADE,
                                                     related_name='text_culturals_agri_product_level2', blank=True,
                                                     null=True)

    cultural_delicacies_level1 = models.ForeignKey(CulturalDelicacies, on_delete=models.CASCADE,
                                                   related_name='text_culturals_delicacies_level1', blank=True,
                                                   null=True)
    cultural_delicacies_level2 = models.ForeignKey(CulturalDelicacies, on_delete=models.CASCADE,
                                                   related_name='text_culturals_delicacies_level2', blank=True,
                                                   null=True)

    cultural_processed_product_level1 = models.ForeignKey(CulturalProcessedProduct, on_delete=models.CASCADE,
                                                          related_name='text_culturals_processed_product_level1',
                                                          blank=True, null=True)
    cultural_processed_product_level2 = models.ForeignKey(CulturalProcessedProduct, on_delete=models.CASCADE,
                                                          related_name='text_culturals_processed_product_level2',
                                                          blank=True, null=True)

    def __str__(self):
        return f"TextCultural: {self.keywords}"


class TextHumanistic(models.Model):
    keywords = models.TextField(blank=True, null=True)
    information_source = models.CharField(max_length=20, choices=SOURCE_CHOICES, blank=True, null=True)
    information_address = models.TextField(blank=True, null=True)
    copyright_owner = models.CharField(max_length=10, choices=COPYRIGHT_CHOICES, default='自有')

    humanistic_category_level1 = models.ForeignKey(HumanisticCategory, on_delete=models.CASCADE,
                                                   related_name='text_humanistics_category_level1', blank=True,
                                                   null=True)
    humanistic_category_level2 = models.ForeignKey(HumanisticCategory, on_delete=models.CASCADE,
                                                   related_name='text_humanistics_category_level2', blank=True,
                                                   null=True)

    humanistic_heritage_level1 = models.ForeignKey(HumanisticHeritage, on_delete=models.CASCADE,
                                                   related_name='text_humanistics_heritage_level1', blank=True,
                                                   null=True)
    humanistic_heritage_level2 = models.ForeignKey(HumanisticHeritage, on_delete=models.CASCADE,
                                                   related_name='text_humanistics_heritage_level2', blank=True,
                                                   null=True)

    humanistic_topic_level1 = models.ForeignKey(HumanisticTopic, on_delete=models.CASCADE,
                                                related_name='text_humanistics_topic_level1', blank=True, null=True)
    humanistic_topic_level2 = models.ForeignKey(HumanisticTopic, on_delete=models.CASCADE,
                                                related_name='text_humanistics_topic_level2', blank=True, null=True)

    def __str__(self):
        return f"TextHumanistic: {self.keywords}"
