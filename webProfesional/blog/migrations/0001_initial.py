# Generated by Django 3.0 on 2022-08-02 15:53

import ckeditor_uploader.fields
import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Contenido')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Imagen')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('slug', models.SlugField(max_length=250)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'unique_together': {('slug',)},
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Titulo')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('portada', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Adjunta una Imagen')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('sliders', models.BooleanField(blank=True, default=False, null=True)),
                ('color_titulo', colorfield.fields.ColorField(blank=True, default='#FFFFFF', max_length=18, null=True, verbose_name='Selecciona Color del Titulo')),
                ('color_subtitulo', colorfield.fields.ColorField(blank=True, default='#FFFFFF', max_length=18, null=True, verbose_name='Selecciona Color del Subtitulo')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_category', to='blog.Category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ('created',),
            },
        ),
    ]