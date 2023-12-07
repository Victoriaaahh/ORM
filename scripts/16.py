import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings") 
django.setup()

from app.models import Usuario, Postagem, Comentario, Reacao

dados_seguidores = [
    {'from_usuario_id': 1, 'to_usuario_id': 2},
    {'from_usuario_id': 2, 'to_usuario_id': 3},
    {'from_usuario_id': 2, 'to_usuario_id': 4},
    {'from_usuario_id': 3, 'to_usuario_id': 2},
    {'from_usuario_id': 3, 'to_usuario_id': 4},
    {'from_usuario_id': 4, 'to_usuario_id': 2},
    {'from_usuario_id': 5, 'to_usuario_id': 4},
    {'from_usuario_id': 6, 'to_usuario_id': 4},
]

# Cadastrando os dados no banco de dados
for dados in dados_seguidores:
    Usuario.objects.get(id=dados['from_usuario_id']).seguindo.add(Usuario.objects.get(id=dados['to_usuario_id']))