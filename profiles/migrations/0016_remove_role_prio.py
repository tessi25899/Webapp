# Generated by Django 3.0.2 on 2020-01-31 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_role_prio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='prio',
        ),
    ]