import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings") 
django.setup()

from app.models import Usuario, Postagem, Comentario

usuarios = Usuario.objects.all()
postagens = Postagem.objects.all()

# Criando comentários para as postagens
comentarios = [
    Comentario(usuario=usuarios[0], postagem=postagens[0], conteudo='Que legal! Compartilhe mais sobre o que aprendeu.'),
    Comentario(usuario=usuarios[1], postagem=postagens[1], conteudo='Concordo! Viajar é uma experiência enriquecedora.'),
    Comentario(usuario=usuarios[2], postagem=postagens[2], conteudo='Quem ganhou a partida? Fiquei curioso!'),
    Comentario(usuario=usuarios[3], postagem=postagens[3], conteudo='Que sorte! Adoraria ter assistido.'),
    Comentario(usuario=usuarios[4], postagem=postagens[4], conteudo='Parabéns pela conquista! Bugs são sempre desafiadores.'),
    Comentario(usuario=usuarios[5], postagem=postagens[5], conteudo='Adoro esse clima para ler. Qual o livro que está lendo?'),
    Comentario(usuario=usuarios[6], postagem=postagens[6], conteudo='Caramba! Como foi a sensação de saltar de paraquedas?'),
    Comentario(usuario=usuarios[1], postagem=postagens[7], conteudo='Natureza sempre surpreendente. Descobriu algo novo?'),
    Comentario(usuario=usuarios[1], postagem=postagens[8], conteudo='Fiquei curioso sobre a receita! Compartilhe conosco.'),
    Comentario(usuario=usuarios[2], postagem=postagens[9], conteudo='Treino pesado é o caminho para a saúde. 💪'),
    Comentario(usuario=usuarios[3], postagem=postagens[10], conteudo='Arte contemporânea é fascinante. Alguma obra em especial chamou sua atenção?'),
]

# Salvando os comentários no banco de dados
Comentario.objects.bulk_create(comentarios)