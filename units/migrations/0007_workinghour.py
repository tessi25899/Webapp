# Generated by Django 3.0.2 on 2020-01-27 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_role_prio'),
        ('units', '0006_auto_20200127_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workinghour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, max_length=15, null=True)),
                ('starttime', models.TimeField(blank=True, null=True)),
                ('endtime', models.TimeField(blank=True, null=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Group')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='units.Unit')),
            ],
        ),
    ]