from django.db import models
from tinymce.models import HTMLField
import uuid


UNIDAD = (
    ('0', 'Nunca'),
    ('1', 'Horas'),
    ('2', 'Días'),
    ('3', 'Semanas'),
    ('4', 'Meses'),
)


class Duracion(models.Model):
    principal = models.CharField('Descripción',max_length=128, blank=True)
    tiempo = models.IntegerField('Tiempo de Expiración', blank=True)
    unidad = models.CharField(max_length=1, choices=UNIDAD)
    activo = models.BooleanField('Activo', max_length=128, blank=True)
    def __str__(self):
        return '%s' % (self.principal)
    class Meta:
        verbose_name_plural = "Tiempo de Duración"


class Codigo(models.Model):
    url = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    codigo = HTMLField('Código',max_length=16384, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    expiracion = models.ForeignKey(Duracion, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Lista de código compartido"
