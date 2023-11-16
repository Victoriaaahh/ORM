import os, sys, django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from app.models import Usuario

usuarios = [
    Usuario(nome='Pedro Santos', usuario='pedro789', senha='P!789senha',
    email='pedro.santos@hotmail.com', apresentacao='E aí, eu sou o Pedro. Adoro esportes e estou sempre em movimento.'),
    Usuario(nome='Ana Pereira', usuario='ana101', senha='Ana*101Senha',
    email='ana.pereira@gmail.com', apresentacao='Oi gente, eu sou a Ana. Sou apaixonada por arte e música.'),
    Usuario(nome='Lucas Oliveira', usuario='lucas202', senha='L@ucas202',
    email='lucas.oliveira@gmail.com', apresentacao='Fala galera, eu sou o Lucas. Amo tecnologia e programação.'),
    Usuario(nome='Gabriela Lima', usuario='gabi303', senha='Gabi@303',
    email='gabi.lima@yahoo.com', apresentacao='Oi, meu nome é Gabriela. Adoro livros e café.'),
    Usuario(nome='Carlos Pereira', usuario='carlos404', senha='Car!os404',
    email='carlos.pereira@hotmail.com', apresentacao='E aí, eu sou o Carlos. Sou fã de esportes radicais e aventuras.'),
]
Usuario.objects.bulk_create(usuarios)