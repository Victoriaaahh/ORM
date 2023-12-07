import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.db.models import Count, Case, When, Value, CharField
from app.models import Usuario, Postagem

usuario_escolhido = Usuario.objects.get(id=4)

numero_postagens_usuario = Postagem.objects.filter(usuario=usuario_escolhido).count()

print(f"{usuario_escolhido.nome} fez {numero_postagens_usuario} postagens.")