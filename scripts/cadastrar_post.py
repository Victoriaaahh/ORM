import os, sys, django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from app.models import Usuario, Postagem

usuarios = Usuario.objects.all()

Postagem.objects.bulk_create([
    Postagem(conteudo='Acabei de voltar de uma viagem incrível! Explorei lugares incríveis e vivi experiências únicas.', usuario=usuarios[0]),
    Postagem(conteudo='Hoje experimentei uma nova receita e ficou maravilhosa! Quem quer a receita completa?', usuario=usuarios[1]),
    Postagem(conteudo='Aventuras radicais hoje! Fui fazer trilha e depois me aventurei em um esporte radical. Adrenalina pura!', usuario=usuarios[2]),
    Postagem(conteudo='Dia relaxante de spa e meditação. Recarregando as energias para a semana que vem.', usuario=usuarios[3]),
    Postagem(conteudo='Participei de um evento cultural hoje. Conheci pessoas incríveis e aprendi muito!', usuario=usuarios[4]),
])

