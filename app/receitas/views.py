from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Receita
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from image_utils import image_reshape


# Create your views here.
def index(request):
    receititas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    paginator = Paginator(receititas, 6)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)
    dados = {'receitas': receitas_por_pagina}
    return render(request, 'receitas/index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receitas/receita.html', receita_a_exibir)
    

def buscar(request):
    receititas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    if 'search' in request.GET:
        nome_a_buscar = request.GET['search']
        receititas = receititas.filter(nome_receita__icontains=nome_a_buscar)
    dados = {'receitas': receititas}
    return render(request, 'receitas/buscar.html', dados)
    

def cria_receita(request):
    if request.method == "POST":
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        foto_receita.file = image_reshape(foto_receita.file)
        if request.POST['publicada'] == "True":
            publicada = True
        else:
            publicada = False
        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(
            pessoa=user,
            nome_receita=nome_receita,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            publicada=publicada,
            foto_receita=foto_receita,
        )
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria_receita.html')
        
def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')
    
    
def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {
        'receita': receita
    }    
    return render(request, 'receitas/edita_receita.html', receita_a_editar)
    
    
def atualiza_receita(request):
    if request.method == "POST":
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            foto_receita = request.FILES['foto_receita']
            foto_receita.file = image_reshape(foto_receita.file)
            r.foto_receita = foto_receita
        if request.POST['publicada'] == "True":
            r.publicada = True
        else:
            r.publicada = False
        r.save()
    return redirect('dashboard')
