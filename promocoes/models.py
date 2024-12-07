from django.db import models

CATEGORIAS = [
    ('ELETRONICO', 'Eletrônico'),
    ('ROUPA', 'Roupa'),
    ('ALIMENTO', 'Alimento')
]

class Promocao(models.Model):
	nome_produto = models.CharField(max_length = 100)
	#data_cadastro = models.DateField(null=True, blank=True)
	descricao = models.TextField()
	preco_original = models.DecimalField(max_digits=10, decimal_places=2)
	preco_promocional = models.DecimalField(max_digits=10, decimal_places=2)
	data_inicio = models.DateTimeField()
	data_termino = models.DateTimeField()
	categoria = models.CharField(max_length=20, choices=CATEGORIAS,null=True)

	class Meta:
		unique_together = ('nome_produto', 'categoria', 'data_inicio', 'data_termino')

	def get_categoria_display(self):
		return dict(CATEGORIAS).get(self.categoria, "Categoria não definida")

	def __str__(self):
		return self.nome_produto if self.nome_produto else "Nome não disponível"



class Empresa(models.Model):
	nome_empresa = models.CharField(max_length = 100)
	email = models.EmailField()
	endereco = models.TextField()
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