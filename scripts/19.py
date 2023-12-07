import os, sys, django
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings") 
django.setup()

from app.models import Usuario, Postagem, Comentario

usuario = Usuario.objects.get(usuario="maria456")

usuarios_que_eu_sigo = usuario.seguindo.all()

postagens_dos_seguidos = Postagem.objects.filter(usuario__in=usuarios_que_eu_sigo)

for postagem in postagens_dos_seguidos:
    print(f'{postagem.usuario.nome} - {postagem.data.strftime("%d-%m-%Y %H:%M:%S")}: {postagem.conteudo}')