from django.db import models
from CoreApp.models import *

# Choices definitions
SEASON_CHOICES = [
    ('春', '春'),
    ('夏', '夏'),
    ('秋', '秋'),
    ('冬', '冬'),
]

VIDEO_CLASS_CHOICES = [
    ('航拍', '航拍'),
    ('地拍', '地拍'),
    ('地拍+航拍', '地拍+航拍'),
    ('棚拍', '棚拍'),
    ('延时', '延时'),
    ('特殊摄影', '特殊摄影')
]

PICTURE_FRAME_CHOICES = [
    ('横屏', '横屏'),
    ('竖屏', '竖屏')
]

COPYRIGHT_CHOICES = [
    ('自有', '自有'),
    ('共有', '共有'),
    ('他人', '他人'),
]

# Define Place-related Video structure
class VideoPlace(models.Model):
    keywords = models.TextField(blank=True, null=True)
    information_address = models.TextField(blank=True, null=True)
    copyright_owner = models.CharField(max_length=10, choices=COPYRIGHT_CHOICES, default='自有')
    # 项目文件名
    dir_name = models.CharField(max_length=255, blank=True, null=True)
    # 名称
    special_name = models.CharField(max_length=255, blank=True, null=True)
    season = models.CharField(max_length=2, choices=SEASON_CHOICES, blank=True, null=True)
    video_class = models.CharField(max_length=10, choices=VIDEO_CLASS_CHOICES, blank=True, null=True)
    picture_frame = models.CharField(max_length=2, choices=PICTURE_FRAME_CHOICES, blank=True, null=True)

    place_location_level1 = models.ForeignKey(PlaceLocation, on_delete=models.CASCADE, related_name='video_places_level1',
                                             blank=True, null=True)
    place_location_level2 = models.ForeignKey(PlaceLocation, on_delete=models.CASCADE, related_name='video_places_level2',
                                              blank=True, null=True)
    place_location_level3 = models.ForeignKey(PlaceLocation, on_delete=models.CASCADE, related_name='video_places_level3',
                                              blank=True, null=True)

    place_natural_level1 = models.ForeignKey(PlaceNatural, on_delete=models.CASCADE, related_name='video_places_level1',
                                             blank=True, null=True)
    place_natural_level2 = models.ForeignKey(PlaceNatural, on_delete=models.CASCADE, related_name='video_places_level2',
                                             blank=True, null=True)
    place_natural_level3 = models.ForeignKey(PlaceNatural, on_delete=models.CASCADE, related_name='video_places_level3',
                                             blank=True, null=True)

    place_humanistic_level1 = models.ForeignKey(PlaceHumanistic, on_delete=models.CASCADE,
                                                related_name='video_places_level1', blank=True, null=True)
    place_humanistic_level2 = models.ForeignKey(PlaceHumanistic, on_delete=models.CASCADE,
                                                related_name='video_places_level2', blank=True, null=True)
    place_humanistic_level3 = models.ForeignKey(PlaceHumanistic, on_delete=models.CASCADE,
                                                related_name='video_places_level3', blank=True, null=True)
    def __str__(self):
        return f"在地视频: {self.keywords}"

# Define Cultural-related Video structure
class VideoCultural(models.Model):
    keywords = models.TextField(blank=True, null=True)
    information_address = models.TextField(blank=True, null=True)
    copyright_owner = models.CharField(max_length=10, choices=COPYRIGHT_CHOICES, default='自有')
    # 项目文件名
    dir_name = models.CharField(max_length=255, blank=True, null=True)
    # 名称
    special_name = models.CharField(max_length=255, blank=True, null=True)
    season = models.CharField(max_length=2, choices=SEASON_CHOICES, blank=True, null=True)
    video_class = models.CharField(max_length=10, choices=VIDEO_CLASS_CHOICES, blank=True, null=True)
    picture_frame = models.CharField(max_length=2, choices=PICTURE_FRAME_CHOICES, blank=True, null=True)

    cultural_agri_product_level1 = models.ForeignKey(CulturalAgriProduct, on_delete=models.CASCADE,
                                                     related_name='video_cultural_level1', blank=True, null=True)
    cultural_agri_product_level2 = models.ForeignKey(CulturalAgriProduct, on_delete=models.CASCADE,
                                                     related_name='video_cultural_level2', blank=True, null=True)

    cultural_delicacies_level1 = models.ForeignKey(CulturalDelicacies, on_delete=models.CASCADE,
                                                   related_name='video_cultural_level1', blank=True, null=True)
    cultural_delicacies_level2 = models.ForeignKey(CulturalDelicacies, on_delete=models.CASCADE,
                                                   related_name='video_cultural_level2', blank=True, null=True)

    cultural_processed_product_level1 = models.ForeignKey(CulturalProcessedProduct, on_delete=models.CASCADE,
                                                          related_name='video_cultural_level1', blank=True, null=True)
    cultural_processed_product_level2 = models.ForeignKey(CulturalProcessedProduct, on_delete=models.CASCADE,
                                                          related_name='video_cultural_level2', blank=True, null=True)
    def __str__(self):
        return f"物产视频: {self.keywords}"


# Define Humanistic-related Video structure
class VideoHumanistic(models.Model):
    keywords = models.TextField(blank=True, null=True)
    information_address = models.TextField(blank=True, null=True)
    copyright_owner = models.CharField(max_length=10, choices=COPYRIGHT_CHOICES, default='自有')
    dir_name = models.CharField(max_length=255, blank=True, null=True)
    special_name = models.CharField(max_length=255, blank=True, null=True)
    season = models.CharField(max_length=2, choices=SEASON_CHOICES, blank=True, null=True)
    video_class = models.CharField(max_length=10, choices=VIDEO_CLASS_CHOICES, blank=True, null=True)
    picture_frame = models.CharField(max_length=2, choices=PICTURE_FRAME_CHOICES, blank=True, null=True)

    humanistic_category_level1 = models.ForeignKey(HumanisticCategory, on_delete=models.CASCADE,
                                                   related_name='video_humanistic_level1', blank=True, null=True)
    humanistic_category_level2 = models.ForeignKey(HumanisticCategory, on_delete=models.CASCADE,
                                                   related_name='video_humanistic_level2', blank=True, null=True)

    humanistic_heritage_level1 = models.ForeignKey(HumanisticHeritage, on_delete=models.CASCADE,
                                                   related_name='video_humanistic_level1', blank=True, null=True)
    humanistic_heritage_level2 = models.ForeignKey(HumanisticHeritage, on_delete=models.CASCADE,
                                                   related_name='video_humanistic_level2', blank=True, null=True)

    humanistic_topic_level1 = models.ForeignKey(HumanisticTopic, on_delete=models.CASCADE,
                                                related_name='video_humanistic_level1', blank=True, null=True)
    humanistic_topic_level2 = models.ForeignKey(HumanisticTopic, on_delete=models.CASCADE,
                                                related_name='video_humanistic_level2', blank=True, null=True)

    def __str__(self):
        return f"文化视频: {self.keywords}"