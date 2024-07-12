from django.db import models

# 在地

# 行政区划
class PlaceLocation(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_locations', null=True, blank=True)

    def __str__(self):
        return self.name

# 自然景观
class PlaceNatural(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_naturals', null=True, blank=True)

    def __str__(self):
        return self.name

# 人文景观
class PlaceHumanistic(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_humanistics', null=True, blank=True)

    def __str__(self):
        return self.name

# 人文

# 文化类别
class HumanisticCategory(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True)

    def __str__(self):
        return self.name

# 文化遗产
class HumanisticHeritage(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_heritages', null=True, blank=True)

    def __str__(self):
        return self.name

# 文化专题
class HumanisticTopic(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_topics', null=True, blank=True)

    def __str__(self):
        return self.name

# 风物
# 初级农产品
class CulturalAgriProduct(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_agri_products', null=True, blank=True)

    def __str__(self):
        return self.name

# 美食
class CulturalDelicacies(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_delicacies', null=True, blank=True)

    def __str__(self):
        return self.name

# 加工食品
class CulturalProcessedProduct(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_processed_products', null=True, blank=True)

    def __str__(self):
        return self.name
