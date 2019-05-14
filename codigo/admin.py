# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from codigo.models import *
from tinymce.models import HTMLField


class Duracion_Admin(admin.ModelAdmin):
    list_display = ("principal","tiempo","unidad","activo")
admin.site.register(Duracion,Duracion_Admin)


class Codigo_Admin(admin.ModelAdmin):
    list_display = ("url","nombre","fecha")
admin.site.register(Codigo,Codigo_Admin)