import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from app.models import Usuario

usuarios_gmail = Usuario.objects.filter(email__icontains='@gmail.com').count()

print(f"Número de usuários com o domínio '@gmail.com': {usuarios_gmail}")