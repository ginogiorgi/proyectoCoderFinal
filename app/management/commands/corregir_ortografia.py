from django.core.management.base import BaseCommand
from app.models import Anime, Manga, Notices
import re

def corregir_texto(texto):
    if not texto:
        return texto
    # Diccionario de correcciones comunes
    correcciones = {
        r'anos': 'años',
        r'ano ': 'año ',
        r'facultad tecnologica': 'Facultad Tecnológica',
        r'ingenieria': 'Ingeniería',
        r'sistemas': 'Sistemas',
        r'programacion': 'programación',
        r'intrigo': 'intrigó',
        r'mas ': 'más ',
        r'curso': 'curso',
        r'rosario': 'Rosario',
        r'cursando': 'cursando',
        r'estudiantes': 'estudiantes',
        r'escuela': 'escuela',
        r'tecnologica': 'Tecnológica',
        r'facultad': 'Facultad',
        r'anos': 'años',
        r'anime ': 'anime ',
        r'manga ': 'manga ',
        r'noticia ': 'noticia ',
        r'noticias': 'noticias',
        r'popular': 'popular',
        r'populares': 'populares',
        r'descripcion': 'descripción',
        r'descripcion ': 'descripción ',
        r'contenido': 'contenido',
        r'titulo': 'título',
        r'usuario': 'usuario',
        r'usuarios': 'usuarios',
        r'perfil': 'perfil',
        r'perfiles': 'perfiles',
        r'estudio': 'estudio',
        r'estudios': 'estudios',
        r'mensaje': 'mensaje',
        r'mensajes': 'mensajes',
    }
    for error, correc in correcciones.items():
        texto = re.sub(error, correc, texto, flags=re.IGNORECASE)
    return texto

class Command(BaseCommand):
    help = 'Corrige errores ortográficos comunes en los textos de la base de datos.'

    def handle(self, *args, **kwargs):
        modelos = [Anime, Manga, Notices]
        for modelo in modelos:
            for obj in modelo.objects.all():
                campos = [f.name for f in modelo._meta.fields if f.get_internal_type() in ['CharField', 'TextField']]
                cambiado = False
                for campo in campos:
                    valor = getattr(obj, campo)
                    nuevo_valor = corregir_texto(valor)
                    if valor != nuevo_valor:
                        setattr(obj, campo, nuevo_valor)
                        cambiado = True
                if cambiado:
                    obj.save()
        self.stdout.write(self.style.SUCCESS('Corrección ortográfica completada.'))
