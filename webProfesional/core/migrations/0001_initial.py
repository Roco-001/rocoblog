# Generated by Django 3.0 on 2022-08-01 17:03

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Slider')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img_sliders', verbose_name='Adjunta la Imagen')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Titulo del Slider')),
                ('color_titulo', colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Selecciona Color del Titulo')),
                ('subtitulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='SubTitulo del Slider')),
                ('color_subtitulo', colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Selecciona Color del Subtitulo')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
                'ordering': ['created'],
            },
        ),
    ]
