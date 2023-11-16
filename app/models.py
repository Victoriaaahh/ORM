from django.db import models

# Create your models here.

from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    usuario = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=60)
    email = models.EmailField(max_length=255)
    apresentacao = models.CharField(max_length=255, null=True)

class Postagem(models.Model):
    id = models.AutoField(primary_key=True)
    conteudo = models.CharField(max_length=140)
    data = models.DateTimeField(default=models.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    conteudo = models.CharField(max_length=140)
    data = models.DateTimeField(default=models.now)

class Reacao(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateTimeField(default=models.now)

    class Meta:
        unique_together = ('postagem', 'usuario')

