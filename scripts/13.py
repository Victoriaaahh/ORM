import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.db.models import Count, Case, When, Value, CharField
from app.models import Postagem, Comentario

#mude o 4 pelo id de quem voce deseja consultar
postagem_escolhida = Postagem.objects.get(id=1)

comentarios_da_postagem = Comentario.objects.filter(postagem=postagem_escolhida)

print(f"Comentários da postagem {postagem_escolhida.id}:")
for comentario in comentarios_da_postagem:
    print(f"ID: {comentario.id}, Conteúdo: {comentario.conteudo}, Data: {comentario.data}")