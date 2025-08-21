from django.shortcuts import render, get_object_or_404
from .models import Receita

def home(request):
    receitas = Receita.objects.all().order_by('-created_at')
    context = {
        'receitas': receitas
    }
    return render(request, 'receitas/home.html', context)

def receita_detail(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    context = {
        'receita': receita,
    }
    return render(request, 'receitas/receita_detail.html', context)