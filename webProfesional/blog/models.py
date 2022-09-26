from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from taggit.managers import TaggableManager
from datetime import date
from colorfield.fields import ColorField
hoy = date.today()


class Category(models.Model):
    name = models.CharField(max_length=100,
        verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True,
        verbose_name="Fecha de creación")
    content = RichTextUploadingField(verbose_name= "Contenido",  null=True, blank=True)

    image = models.ImageField(upload_to="category", null=True, blank=True,
        verbose_name="Imagen")

    updated = models.DateTimeField(auto_now=True,
        verbose_name="Fecha de edición")

    slug = models.SlugField(max_length=250)

    class Meta:
        unique_together = ('slug', )
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category',
                       args=[self.id,
                           self.slug])





# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
            .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title = models.CharField(max_length=250, verbose_name='Titulo')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    portada = models.ImageField(verbose_name='Adjunta una Imagen', upload_to='blog', blank=True, null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = RichTextUploadingField(verbose_name='Contenido')
    publish = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='blog_category')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Nuestro modelo personalizado PublishedManager
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    visit = models.IntegerField(verbose_name='cantidad de visitas', default=0)

    #si es sliders
    sliders = models.BooleanField(default=False, blank=True, null=True)
    color_titulo = ColorField(verbose_name="Selecciona Color del Titulo", blank=True, null=True,default='#FFFFFF')
    color_subtitulo = ColorField(verbose_name="Selecciona Color del Subtitulo", blank=True, null=True,default='#FFFFFF')
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.id,
                           self.slug])


    def numeroTicket(self):
        return (str(self.id).zfill(8))

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'



class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='repuesta')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.comment}'