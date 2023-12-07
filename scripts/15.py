import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.db.models import Count, Case, When, Value, CharField
from app.models import Postagem

postagem_mais_curtida = Postagem.objects.annotate(numero_reacoes=Count('reacao')).order_by('-numero_reacoes').first()

if postagem_mais_curtida:
    print(f"A postagem mais curtida do site é a de ID {postagem_mais_curtida.id} com {postagem_mais_curtida.numero_reacoes} curtidas.")
else:
    print("Não há postagens no site.")