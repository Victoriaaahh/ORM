import os, sys, django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from app.models import Usuario

usuarios = Usuario.objects.values_list('nome', 'email')

for usuario in usuarios:
    print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")
