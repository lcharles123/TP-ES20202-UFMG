from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template import RequestContext


from django.views.decorators.csrf import csrf_exempt #desativar protecao para receber os dados sem cookie de verificacao
from django.http import HttpResponse

from .models import *
import time, random, string
# view eh o esqueleto, cada funcao abaixo define como a pagina eh obtida, um request pode ser feito em determinado link e os arquivos url.py mapeiam para essa funcao  

def dashboard(request):
    #colocar aqui as funcoes para obter os dados dinamicos quando carregados a pagina index, ex. lista de dispositivos
    # Number of visits to this view, as counted in the session variable.
    
    InstanciaLink = Links()
    
    InstanciaLink.nomeLink='nome link test 1'
    InstanciaLink.chaveLink='123'
    print(InstanciaLink.dispID)
    # Salve o objeto no banco de dados.
    #InstanciaLink.save()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1
	
    request_context = RequestContext(request)
    request_context.push({"links": "links"})
	
    chave = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
 
    #print(chave)
    print("dashboard");
    disp = InstanciaLink
    context = {
        'lista_de_links': disp, #tipo QuerySet, uma tabela de banco de dados.
    }
    
    #/ myapplication / mymodelname / 2  #instanciar assim
    
    # Render the HTML template index.html with the data in the context variable.    
    return render(
        request,
        'index.html',
        context # dict, forma de passar variaveis para o arquivo html
    )


# esqueleto do formulario para cadastro, link para esta funcao: dashboard/signup
def  signup(request):

    if request.method == 'GET':
        print("signup");
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def  links(request):
    if request.method == 'GET':
        print("links")
         
    return render(request, 'links.html')


def  graficos(request):
    if request.method == 'GET':
        print("graficos")
    
    
    

    return render(request, 'graficos.html' )


def  ajuda(request):

    if request.method == 'GET':
        print("signup")
    return render(request, 'ajuda.html')


def  conta(request):

    if request.method == 'GET':
        print("signup")
    return render(request, 'conta.html')
    
@csrf_exempt #decorador que permite requesicoes sem controle por cookie
def api(request):
    #print(help(request))
    if request.method == 'POST':
        chave = request.get_full_path().split("=",1)[1] #obter a chave 
        dado = (list(request.POST.items())[0])[1] #obter segundo elemento da tupla('temp','valor')
        print("url completa: " + request.get_full_path() )
        print(chave)
        print(dado)
        print(time.ctime())
        return HttpResponse('dado recebido, obrigado\r\n')
    
    return HttpResponse('erro, requisicao deve ser POST\r\n')

def  logout(request):

    if request.method == 'GET':
        django_logout(request)
        print("logout")
    return render(request, 'logout.html')


