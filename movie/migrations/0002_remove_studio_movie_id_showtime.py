# Generated by Django 4.1 on 2022-09-08 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studio',
            name='movie_id',
        ),
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='movie.movie')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studio', to='movie.studio')),
            ],
        ),
    ]
