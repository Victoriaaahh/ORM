import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings") 
django.setup()

from app.models import Usuario, Postagem, Comentario

usuario = Usuario.objects.get(usuario="ana101") # joao123, maria456, ana101
quantidade_seguidores = usuario.seguidores.count()
print(f'O usuário "{usuario.nome}" é seguido por {quantidade_seguidores} usuários.')