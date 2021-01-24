from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from receitas.models import Receita

# Create your views here.
def cadastro(request):
    
    if request.method == 'POST':
        
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        
        if not nome.strip():
            # print()
            return redirect('cadastro')
            
        if not email.strip():
            # print()
            return redirect('cadastro')
            
        if not senha.strip():
            # print()
            return redirect('cadastro')
            
        if senha != senha2:
            # print()
            return redirect('cadastro')
            
        if User.objects.filter(email=email).exists():
            # print()
            return redirect('cadastro')
            
        user = User.objects.create_user(nome, email, senha)
        user.save()
        print('usiario cadastrado com sucesso')
        print(nome, email, senha)
        
        return render(request, "usuarios/login.html")
        
    else:
        return render(request, 'usuarios/cadastro.html')
        

def login(request):
    
    if request.method == 'POST':
        
        email = request.POST['email']
        senha = request.POST['senha']
        
        if (not email.strip()) or (not senha.strip()):
            print('POST inválido')
            return redirect('login')
    
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                print('login deu boa')
                
                teste = {
                    'teste1': 'valor da chave teste1',
                }
                
        
                return redirect('dashboard')
                
            else:
                return redirect('login')
    
    else:
        return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)
        dados = {
            'receitas': receitas
        }
        
        return render(request, 'usuarios/dashboard.html', dados)
        
    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')


