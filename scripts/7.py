import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from app.models import Postagem
from datetime import datetime

# Obtendo a data de início e fim do ano de 2023
inicio_2023 = datetime(2023, 1, 1)
fim_2023 = datetime(2023, 12, 31, 23, 59, 59)

# Contando as postagens realizadas no ano de 2023
postagens_2023 = Postagem.objects.filter(data__range=(inicio_2023, fim_2023))
quantidade_postagens_2023 = postagens_2023.count()

# Imprimindo a quantidade de postagens
print(f"Quantidade de postagens em 2023: {quantidade_postagens_2023}")
