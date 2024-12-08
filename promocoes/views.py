from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Empresa, Promocao, Categoria

# Create your views here.
def home(request):
	categorias = Categoria.objects.all()  # Recupera todas as categorias do banco	
	empresas = Empresa.objects.all()
	promocoes = Promocao.objects.all()  # Recupera todas as promoções do banco
	return render(request, 'home.html', {'categorias': categorias, 'empresas': empresas, 'promocoes': promocoes})


def promofacil(request):
    return render(request, 'promofacil.html')  


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


def criar_promocao(request):
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        preco_original = request.POST.get('preco_original')
        preco_promocional = request.POST.get('preco_promocional')
        data_inicio = request.POST.get('data_inicio')
        data_termino = request.POST.get('data_termino')
        categoria = request.POST.get('categoria')
        imagem = request.FILES.get('imagem')

        # Verifique se todos os dados foram recebidos
        if not imagem:
            return HttpResponse("Erro: Imagem não foi enviada corretamente.")

        promocao = Promocao(
            nome_produto=nome_produto,
            preco_original=preco_original,
            preco_promocional=preco_promocional,
            data_inicio=data_inicio,
            data_termino=data_termino,
            categoria=categoria,
            imagem=imagem
        )
        promocao.save()
        return HttpResponse("Promoção cadastrada com sucesso!")

    return render(request, 'cadastroPromocao.html')

