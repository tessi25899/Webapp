# Generated by Django 3.0.2 on 2020-01-26 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20200117_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='prio',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
