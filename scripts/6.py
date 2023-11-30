import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from datetime import datetime, timedelta
from app.models import Postagem

# Calculando a data atual
data_atual = datetime.now()

# Calculando a data do último mês
ultimo_mes = data_atual - timedelta(days=30)

# Obtendo o primeiro dia do mês atual
primeiro_dia_do_mes_atual = datetime(data_atual.year, data_atual.month, 1)

# Obtendo as postagens realizadas no último mês
postagens_ultimo_mes = Postagem.objects.filter(data__gte=primeiro_dia_do_mes_atual, data__lt=data_atual)

# Iterando sobre as postagens e imprimindo o conteúdo e a data
for postagem in postagens_ultimo_mes:
    print(f"Conteúdo: {postagem.conteudo}")
    print(f"Data: {postagem.data}")
