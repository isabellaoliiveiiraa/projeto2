from django.shortcuts import render
from django.http import Http404


# Create your views here.
def home(request):
    return render(request, 'receitas/home.html')

def receita(request, receita_id):

    context = {
        'receita_id': id,
        'receita_title': f'receita detalhada{id}',
        'receita_description': f'esta é a descrição detalhada da receita com id {id}',
    }