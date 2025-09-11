from django.shortcuts import render, get_object_or_404
from .models import Receita

def home(request):
    categoria_selecionada = request.GET.get('categoria')
    categorias_disponiveis = Receita.CATEGORIAS

    if categoria_selecionada:
        receitas = Receita.objects.filter(categoria=categoria_selecionada)
    else:
        receitas = Receita.objects.all()

    contexto = {
        'receitas': receitas,
        'categorias': categorias_disponiveis,
        'categoria_selecionada': categoria_selecionada,
    }
    
    return render(request, 'receitas/home.html', contexto)

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receitas/receita_detail.html', {'receita': receita})

def pesquisar_receitas(request):
    query = request.GET.get('q', '')
    
    if query:
        resultados = Receita.objects.filter(title__icontains=query)
    else:
        resultados = []
        
    contexto = {
        'query': query,
        'receitas': resultados
    }
    
    return render(request, 'receitas/pesquisa.html', contexto)