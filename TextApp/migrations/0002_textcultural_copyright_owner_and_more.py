# Generated by Django 5.0.6 on 2024-07-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textcultural',
            name='copyright_owner',
            field=models.CharField(choices=[('自有', '自有'), ('共有', '共有'), ('他人', '他人')], default='自有', max_length=10),
        ),
        migrations.AddField(
            model_name='texthumanistic',
            name='copyright_owner',
            field=models.CharField(choices=[('自有', '自有'), ('共有', '共有'), ('他人', '他人')], default='自有', max_length=10),
        ),
        migrations.AddField(
            model_name='textplace',
            name='copyright_owner',
            field=models.CharField(choices=[('自有', '自有'), ('共有', '共有'), ('他人', '他人')], default='自有', max_length=10),
        ),
    ]
