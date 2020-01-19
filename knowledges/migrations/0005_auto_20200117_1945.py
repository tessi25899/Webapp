# Generated by Django 3.0.2 on 2020-01-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledges', '0004_auto_20200117_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledge',
            name='ordernumber',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='ordernumber',
            field=models.IntegerField(),
        ),
    ]
