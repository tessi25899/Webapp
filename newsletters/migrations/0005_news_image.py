# Generated by Django 3.0.2 on 2020-01-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0004_auto_20200119_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images'),
        ),
    ]