# Generated by Django 3.0.2 on 2020-01-06 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledges', '0002_auto_20200106_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='fwdv',
            name='fwdv',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
