# Generated by Django 3.0.2 on 2020-01-17 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20200115_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(blank=True, default=4, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Role'),
        ),
    ]
