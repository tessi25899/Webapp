# Generated by Django 3.0.2 on 2020-01-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20200114_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='forall',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]