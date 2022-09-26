from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


# Create your models here.

class Equipo(models.Model):
    name = models.CharField(max_length=100,
        verbose_name="Nombre")
    cargo = models.CharField(max_length=100,
                            verbose_name="Cargo")
    content = RichTextUploadingField(verbose_name= "Contenido",  null=True, blank=True)
    image = models.ImageField(upload_to="about", null=True, blank=True,
        verbose_name="Imagen")
    updated = models.DateTimeField(auto_now=True,
        verbose_name="Fecha de edición")

    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self):
        return self.name



class About(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)

    titulo1 = models.CharField(max_length=200, verbose_name="Primer Titulo", blank=True, null=True)
    subtitulo1 = RichTextUploadingField(verbose_name="Primer Parrafo", blank=True, null=True)
    imagen1 = models.ImageField(verbose_name='Adjunta la primera imagen', upload_to= 'about', blank=True, null=True)

    titulo2 = models.CharField(max_length=200, verbose_name="Segundo Titulo", blank=True, null=True)
    subtitulo2 = RichTextUploadingField(verbose_name="Segundo Parrafo", blank=True, null=True)
    imagen2 = models.ImageField(verbose_name='Adjunta la Segundo imagen', upload_to='about', blank=True, null=True)

    imagen3 = models.ImageField(verbose_name='Tercera Imagen', upload_to= 'opening', blank=True, null=True)
    imagen4 = models.ImageField(verbose_name='Cuarta Imagen', upload_to='opening', blank=True, null=True)
    titulo3 = models.CharField(max_length=200, verbose_name="Tercer Titulo", blank=True, null=True)
    subtitulo3 = RichTextUploadingField(verbose_name="Tercer parrafo", blank=True, null=True)

    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='get_equipos')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Acerca de"
        verbose_name_plural = "Acerca de Nosotros"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name