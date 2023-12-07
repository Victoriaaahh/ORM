import os, sys, django
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings") 
django.setup()

from app.models import Usuario, Postagem, Comentario

usuario = Usuario.objects.get(usuario="maria456")  

seguidos_por_mim = usuario.seguindo.all()

seguidores_do_meu_usuario = usuario.seguidores.all()

amigos = seguidos_por_mim.intersection(seguidores_do_meu_usuario)

for amigo in amigos:
    print(amigo.nome)