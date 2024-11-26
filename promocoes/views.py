from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Empresa,Produto
from decimal import Decimal

# Create your views here.

def home(request):
	if request.session.get('usuario'):
		return HttpResponse('PÁGINA HOME')
	else:
		return redirect('/auth/login/?status=2')

def criar_produto(request):
	nome_produto = request.POST.get("nome_produto")
	preco_original = request.POST.get("preco_original")
	preco_promocional = request.POST.get("preco_promocional")
	descricao = request.POST.get("descricao")

	# Garantir que os valores numéricos sejam convertidos corretamente, tratando vazios ou None
	if preco_original not in (None, ''):
		preco_original = Decimal(preco_original)
	else:
		preco_original = None

	if preco_promocional not in (None, ''):
		preco_promocional = Decimal(preco_promocional)
	else:
		preco_promocional = None

	produto = Produto(nome_produto=nome_produto,
					  preco_original =preco_original,
					  preco_promocional=preco_promocional,
					  descricao=descricao)
	produto.save()
	return render(request, 'cadastroProduto.html')

def criar_empresa(request):
	nome_empresa = request.POST.get("nome_empresa")
	email = request.POST.get("email")
	endereco = request.POST.get("endereco")
	telefone = request.POST.get("telefone")

	empresa = Empresa(nome_empresa=nome_empresa,
					  email =email,
					  endereco=endereco,
					  telefone=telefone)
	empresa.save()
	return render(request, 'cadastroEmpresa.html')
