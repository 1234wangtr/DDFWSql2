# Generated by Django 5.0.6 on 2024-07-12 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CoreApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextCultural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(blank=True, null=True)),
                ('information_source', models.CharField(blank=True, choices=[('地道风物', '地道风物'), ('图书', '图书'), ('专家', '专家'), ('网络', '网络')], max_length=20, null=True)),
                ('information_address', models.TextField(blank=True, null=True)),
                ('cultural_agri_product_level1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_culturals_agri_product_level1', to='CoreApp.culturalagriproduct')),
                ('cultural_agri_product_level2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_culturals_agri_product_level2', to='CoreApp.culturalagriproduct')),
                ('cultural_delicacies_level1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_culturals_delicacies_level1', to='CoreApp.culturaldelicacies')),
                ('cultural_delicacies_level2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_culturals_delicacies_level2', to='CoreApp.culturaldelicacies')),
                ('cultural_processed_product_level1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_culturals_processed_product_level1', to='CoreApp.culturalprocessedproduct')),
                ('cultural_processed_product_level2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_culturals_processed_product_level2', to='CoreApp.culturalprocessedproduct')),
            ],
        ),
        migrations.CreateModel(
            name='TextHumanistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(blank=True, null=True)),
                ('information_source', models.CharField(blank=True, choices=[('地道风物', '地道风物'), ('图书', '图书'), ('专家', '专家'), ('网络', '网络')], max_length=20, null=True)),
                ('information_address', models.TextField(blank=True, null=True)),
                ('humanistic_category_level1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_humanistics_category_level1', to='CoreApp.humanisticcategory')),
                ('humanistic_category_level2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_humanistics_category_level2', to='CoreApp.humanisticcategory')),
                ('humanistic_heritage_level1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_humanistics_heritage_level1', to='CoreApp.humanisticheritage')),
                ('humanistic_heritage_level2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_humanistics_heritage_level2', to='CoreApp.humanisticheritage')),
                ('humanistic_topic_level1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_humanistics_topic_level1', to='CoreApp.humanistictopic')),
                ('humanistic_topic_level2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_humanistics_topic_level2', to='CoreApp.humanistictopic')),
            ],
        ),
        migrations.CreateModel(
            name='TextPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(blank=True, null=True)),
                ('information_source', models.CharField(blank=True, choices=[('地道风物', '地道风物'), ('图书', '图书'), ('专家', '专家'), ('网络', '网络')], max_length=20, null=True)),
                ('information_address', models.TextField(blank=True, null=True)),
                ('place_humanistic_level1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_places_humanistic_level1', to='CoreApp.placehumanistic')),
                ('place_humanistic_level2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_places_humanistic_level2', to='CoreApp.placehumanistic')),
                ('place_humanistic_level3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_places_humanistic_level3', to='CoreApp.placehumanistic')),
                ('place_location_level1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_places_location_level1', to='CoreApp.placelocation')),
                ('place_location_level2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_places_location_level2', to='CoreApp.placelocation')),
                ('place_location_level3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_places_location_level3', to='CoreApp.placelocation')),
                ('place_natural_level1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_places_natural_level1', to='CoreApp.placenatural')),
                ('place_natural_level2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_places_natural_level2', to='CoreApp.placenatural')),
                ('place_natural_level3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_places_natural_level3', to='CoreApp.placenatural')),
            ],
        ),
    ]
