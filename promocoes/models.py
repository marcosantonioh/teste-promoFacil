from django.db import models

CATEGORIAS = [
    ('ELETRONICO', 'Eletrônico'),
    ('ROUPA', 'Roupa'),
    ('ALIMENTO', 'Alimento')
]

class Promocao(models.Model):
	nome_produto = models.CharField(max_length = 100)
	data_cadastro = models.DateField()
	descricao = models.TextField()
	preco_original = models.DecimalField(max_digits=10, decimal_places=2)
	preco_promocional = models.DecimalField(max_digits=10, decimal_places=2)
	data_inicio = models.DateTimeField()
	data_termino = models.DateTimeField()
	disponibilidade = models.BooleanField(default=True)
	categoria = models.CharField(max_length=20, choices=CATEGORIAS)

	def __str__(self):
		return self.nome_produto

class Produto(models.Model):
	nome_produto = models.CharField(max_length = 100,null=True, blank=True)
	preco_original = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
	preco_promocional = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
	descricao = models.TextField(null=True, blank=True)


	def __str__(self):
		return self.nome_produto if self.nome_produto else "Nome não disponível"

class Empresa(models.Model):
	nome_empresa = models.CharField(max_length = 100,null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	endereco = models.TextField(null=True, blank=True)
	telefone = models.CharField(max_length = 20, default = "",null=True, blank=True)

	def __str__(self):
			# Verifique se o nome está vazio. Retorne outra informação se necessário.
			if self.nome_empresa:
				return self.nome_empresa
			elif self.email:
				return f"Empresa com email: {self.email}"
			else:
				return "Empresa sem informações"
