from django.db import models

class registro(models.Model):
	nome = models.CharField(max_length=200)
	data_nascimento = models.DateField()
	profissão = models.CharField(max_length=200)
	telefone = models.IntegerField()
	cpf = models.IntegerField()


class cadastro(models.Model):
	nome = models.CharField( max_length=200)
	email = models.EmailField( max_length=200)
	senha = models.CharField( max_length=50)
	confirmar_senha = models.CharField(max_length=50)

	
