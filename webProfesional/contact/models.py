from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)
    email = models.EmailField(verbose_name="Correo", blank=True, null=True)
    subject = models.CharField(max_length=200,verbose_name="Asunto", blank=True, null=True)
    content = models.TextField(max_length=1000, verbose_name="Contenido", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]
