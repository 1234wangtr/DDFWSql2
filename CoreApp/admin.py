from django.contrib import admin
from .models import (
    PlaceLocation, PlaceNatural, PlaceHumanistic,
    HumanisticCategory, HumanisticHeritage, HumanisticTopic,
    CulturalAgriProduct, CulturalDelicacies, CulturalProcessedProduct
)

admin.site.register(PlaceLocation)
admin.site.register(PlaceNatural)
admin.site.register(PlaceHumanistic)
admin.site.register(HumanisticCategory)
admin.site.register(HumanisticHeritage)
admin.site.register(HumanisticTopic)
admin.site.register(CulturalAgriProduct)
admin.site.register(CulturalDelicacies)
admin.site.register(CulturalProcessedProduct)
