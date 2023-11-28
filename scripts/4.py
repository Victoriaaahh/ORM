import os, sys, django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from app.models import Postagem

postagens = Postagem.objects.all().order_by('-data')

for postagem in postagens:
    print(f"Conteúdo: {postagem.conteudo}, Data: {postagem.data}")
