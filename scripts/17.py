import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings") 
django.setup()

from app.models import Usuario, Postagem

usuario_escolhido = Usuario.objects.get(id=1)

postagens_do_usuario = Postagem.objects.filter(usuario=usuario_escolhido)

print(f"Postagens de {usuario_escolhido.nome}:")
for postagem in postagens_do_usuario:
    print(f"ID: {postagem.id}, Conteúdo: {postagem.conteudo}, Data: {postagem.data}")