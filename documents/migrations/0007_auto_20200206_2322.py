# Generated by Django 3.0.2 on 2020-02-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20200205_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedocument',
            name='document',
            field=models.FileField(upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='filedocument',
            name='published',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
