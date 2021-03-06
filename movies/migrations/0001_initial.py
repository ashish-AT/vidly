# Generated by Django 3.1.1 on 2020-09-16 15:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('released_year', models.IntegerField()),
                ('number_in_stock', models.IntegerField()),
                ('daily_rate', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
        ),
    ]
