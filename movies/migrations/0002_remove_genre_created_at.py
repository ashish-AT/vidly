# Generated by Django 3.1.1 on 2020-09-16 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='created_at',
        ),
    ]
