import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.db.models import Count, Case, When, Value, CharField
from app.models import Postagem, Reacao, Usuario

postagem_escolhida = Postagem.objects.get(id=1)

reacoes_da_postagem = Reacao.objects.filter(postagem=postagem_escolhida)

print(f"Reações à postagem {postagem_escolhida.id}:")
for reacao in reacoes_da_postagem:
    print(f"ID do Usuário: {reacao.usuario.id}, Nome do Usuário: {reacao.usuario.nome}")