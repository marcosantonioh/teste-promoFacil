from django.db import models

class Promocao(models.Model):
    nome_produto = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco_original = models.FloatField(default=0)
    preco_promocional = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_produto}"




class Empresa(models.Model):
	nome_empresa = models.CharField(max_length=255, null=False, default="Nome da Empresa")
	email = models.EmailField(default="default@example.com")
	endereco = models.TextField(max_length=255, null=False, default="Endereço Padrão")
	telefone = models.CharField(max_length = 20, default = "")

	def __str__(self):
			# Verifique se o nome está vazio. Retorne outra informação se necessário.
			if self.nome_empresa:
				return self.nome_empresa
			elif self.email:
				return f"Empresa com email: {self.email}"
			else:
				return "Empresa sem informações"



class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome