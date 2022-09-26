from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(About)
class AboutProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')


@admin.register(Equipo)
class EquipooProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')