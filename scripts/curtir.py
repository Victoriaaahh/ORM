import os, sys, django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from app.models import Usuario, Postagem, Reacao

usuarios = Usuario.objects.all()
post = Postagem.objects.get(id = 1)

reacoes = [
    Reacao(usuario=usuarios[3], postagem=post),
    Reacao(usuario=usuarios[1], postagem=post),
    Reacao(usuario=usuarios[2], postagem=post),
    # Adicione outras reações conforme necessário
]

Reacao.objects.bulk_create(reacoes)


