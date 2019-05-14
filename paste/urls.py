from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from codigo import views
from codigo.forms import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('<uuid:url>/',views.Detalles),
    path('editar/<uuid:url>/',views.Editar),
    path('eliminar/<uuid:url>/',views.Eliminar),
    url(r'^$', views.Insertar),

]
admin.site.site_header = "Compartiendo Código."
admin.site.site_title = "PasteCode"
admin.site.index_title = "Bienvenido a PasteCode."

handler404 = 'codigo.views.handler404'
handler500 = 'codigo.views.handler500'