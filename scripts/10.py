import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.db.models import Count, Case, When, Value, CharField
from app.models import Usuario

contagem_por_dominio = Usuario.objects.annotate(
    dominio_email=Case(
        When(email__icontains='@gmail.com', then=Value('Gmail')),
        When(email__icontains='@yahoo.com', then=Value('Yahoo')),
        When(email__icontains='@outlook.com', then=Value('Outlook')),
        default=Value('Outro'), 
        output_field=CharField(),
    )
).values('dominio_email').annotate(total=Count('id')).order_by('-total')

for resultado in contagem_por_dominio:
    print(f"Domínio: {resultado['dominio_email']}, Total de Usuários: {resultado['total']}")