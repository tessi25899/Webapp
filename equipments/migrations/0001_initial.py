# Generated by Django 3.0.2 on 2020-01-20 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('units', '0005_auto_20200111_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=256)),
                ('nominal_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Crewgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('size', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Toolgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiclegroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('radio_name', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('feature', models.TextField(blank=True, null=True)),
                ('water_tank', models.IntegerField(blank=True, null=True)),
                ('construction_date', models.DateField()),
                ('producer', models.CharField(blank=True, max_length=256, null=True)),
                ('power', models.CharField(blank=True, max_length=256, null=True)),
                ('petrol_tank', models.CharField(blank=True, max_length=256, null=True)),
                ('ton', models.CharField(blank=True, max_length=256, null=True)),
                ('length', models.CharField(blank=True, max_length=256, null=True)),
                ('width', models.CharField(blank=True, max_length=256, null=True)),
                ('heigth', models.CharField(blank=True, max_length=256, null=True)),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.Crewgroup')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='units.Unit')),
                ('vehiclegroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipments.Vehiclegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('toolgroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipments.Toolgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Stocktaking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_stock', models.IntegerField()),
                ('date', models.DateField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.Assignment')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.Tool'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.Vehicle'),
        ),
    ]
