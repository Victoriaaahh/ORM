import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from app.models import Comentario

id_da_postagem = 1

# Obtendo os três comentários mais recentes para uma postagem específica
comentarios_recentes = Comentario.objects.filter(postagem__id=id_da_postagem) \
    .order_by('-data')[:3]

# Iterando sobre os comentários e imprimindo o conteúdo e a data
for comentario in comentarios_recentes:
    print(f"Conteúdo: {comentario.conteudo}")
    print(f"Data: {comentario.data}")
