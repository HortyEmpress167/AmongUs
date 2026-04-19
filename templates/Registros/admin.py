from django.contrib import admin
from .models import Alumnos
from .models import Comentario
# Register your models here.
from django.contrib import admin
from .models import ComentarioContacto


class AdministradorModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera','turno')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')

    list_per_page=2
    list_display_links=('matricula', 'nombre')
    list_editable=('turno',)

    def get_readonly_fields(self, request, obj=None):
        # si el usuario pertenece al grupo de permisos "Usuarios"
        if request.user.groups.filter(name="Usuarios").exists():
            # Bloquea los campos
            return ('matricula', 'carrera', 'turno')
        else:
            # Cualquier otro usuario que no pertenece al grupo "Usuarios"
            return ('created', 'updated')

admin.site.register(Alumnos, AdministradorModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
