import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from app.models import Usuario
# Obtendo usuários com palavras-chave na bio
usuarios_com_palavras_chave = Usuario.objects.filter(
    apresentacao__icontains='programação') | Usuario.objects.filter(
    apresentacao__icontains='dev') | Usuario.objects.filter(
    apresentacao__icontains='código'
)

# Iterando sobre os usuários e imprimindo seus detalhes
for usuario in usuarios_com_palavras_chave:
    print(f"Nome: {usuario.nome}")
    print(f"Bio: {usuario.apresentacao}")
