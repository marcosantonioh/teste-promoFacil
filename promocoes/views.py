from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Empresa,Produto
from decimal import Decimal
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

# def home(request):
# 	if request.session.get('usuario'):
# 		return HttpResponse('PÁGINA HOME')
# 	else:
# 		return redirect('/auth/login/?status=2')

def criar_produto(request):
    nome_produto = request.POST.get("nome_produto")
    preco_original = request.POST.get("preco_original")
    preco_promocional = request.POST.get("preco_promocional")
    descricao = request.POST.get("descricao")

    # Validação: Checar se os campos obrigatórios estão preenchidos
    if not nome_produto or not preco_original or not preco_promocional or not descricao:
        return render(request, 'cadastroProduto.html', {
            'erro': 'Todos os campos são obrigatórios!'
        })

    try:
        # Conversão de valores numéricos
        preco_original = Decimal(preco_original)
        preco_promocional = Decimal(preco_promocional)
    except Exception as e:
        return render(request, 'cadastroProduto.html', {
            'erro': 'Os preços devem ser números válidos!'
        })

    # Criar e salvar o produto
    produto = Produto(
        nome_produto=nome_produto,
        preco_original=preco_original,
        preco_promocional=preco_promocional,
        descricao=descricao
    )
    produto.save()

    return render(request, 'cadastroProduto.html', {
        'mensagem': 'Produto cadastrado com sucesso!'
    })




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
