import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings") 
django.setup()

from app.models import Usuario, Postagem, Comentario

from django.db.models import Count

postagem_mais_curtida = Postagem.objects.annotate(num_reacoes=Count('reacao')).order_by('-num_reacoes').first()

print(postagem_mais_curtida.id)