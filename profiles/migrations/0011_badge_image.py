# Generated by Django 3.0.2 on 2020-01-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_profile_motivation'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]