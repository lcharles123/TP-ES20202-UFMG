from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from django.views.decorators.csrf import csrf_exempt #desativar protecao para receber os dados sem cookie de verificacao
from django.http import HttpResponse

from .models import *
import time, random, string

import pandas as pd
import matplotlib.pyplot as plt
# view eh o esqueleto, cada funcao abaixo define como a pagina eh obtida, um request pode ser feito em determinado link e os arquivos url.py mapeiam para essa funcao  

#obtem o pandas dataframe a partir da classe do modelo
def obter_data_frame(classeModelo):
    return pd.DataFrame(list(classeModelo.objects.all().values()))

def dashboard(request):
    #Dispositivos.objects.all().delete() # remove tudo para resetar o banco
    #Links.objects.all().delete() # remove tudo para resetar o banco
    
    df = obter_data_frame(Links)

    dfdisp = obter_data_frame(Dispositivos)
  
    templatePath = 'dashboard/templates/'
    
    if df.empty == False :
        df1 = df.loc[df['userName'] == request.user.username]
        if df1.empty == False :
            df1.to_html(templatePath +'tabela.html',header=True, index=False, columns=['id','chaveLink'])
        if dfdisp.empty == False :
            dfdisp.to_html(templatePath +'tabeladisp.html',header=True, index=False, columns=['linkID_id','timeStamp','dado'])
    else:
        df.to_html(templatePath +'tabela.html')        
    
    print("dashboard");
    
    # Render the HTML template index.html with the data in the context variable.    
    return render( request, 'index.html')

def addlink(request):
    
    instancia = Links(userName=request.user.username, nomeLink='')
    instancia.chaveLink = 'http://localhost:8000/dashboard/api?key=' + get_random_string(length=16)
    context = {'linkAdicionado' : instancia.chaveLink }    
    instancia.save()
    
    print('addlink')
    return render(
        request,
        'addlink.html',
        context
    )

def removelink(request):
    df = obter_data_frame(Links)
    df1 = pd.DataFrame()
    if df.empty == False :
        df1 = df.loc[df['userName'] == request.user.username]
        if df1.empty == False :
            df2 = df1.iloc[-1]['id']
            print('delete ')
            print(df2)
            Links.objects.filter(id=df2).delete()
    
    return render(
        request,
        'removelink.html'
    )

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
            print(username)
            print(password)
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
        df=obter_data_frame(Dispositivos)
        print(df)
        plt.plot(df['dado'])
        plt.title('Dados do dispositivo')
        plt.savefig('dashboard/static/grafico.png')
    return render(request, 'graficos.html' )

def  acoes(request):
    if request.method == 'GET':
        print("acoes")

    return render(request, 'acoes.html' )


def  ajuda(request):

    if request.method == 'GET':
        print("ajuda")
    return render(request, 'ajuda.html')


def conta(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Senha atualizada!')
            return redirect('change_password') # para reverse matching em urls.py
        else:
            messages.error(request, 'Por favor corrija a senha.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

    
@csrf_exempt #decorador que permite requesicoes sem controle por cookie
def api(request):
    #print(help(request))
    if request.method == 'POST':
        chaveRec = request.get_full_path().split("=",1)[1] #obter a chave 
        dado = (list(request.POST.items())[0])[1] #obter segundo elemento da tupla('temp','valor')
      
        lista = obter_data_frame(Links)['chaveLink'].tolist()
        listaChaves = [i.split('=')[1] for i in lista] 
        chaveEstrangeira = 0
        
        if chaveRec in listaChaves: #se dado esta na lista
            listaIndices = obter_data_frame(Links)['id'].tolist() # lista de ids para obter o a chave estrangeira
            for i, j in enumerate(listaChaves):
                if j == chaveRec:
                    chaveEstrangeira = listaIndices[i]
            
            instanciaDisp = Dispositivos(linkID = Links.objects.get(id=chaveEstrangeira)) # FK id na tabela Links
            instanciaDisp.dado = dado          
            instanciaDisp.save()
            
        else:
            return HttpResponse('erro, link invalido\r\n')        

        return HttpResponse('dado recebido, obrigado\r\n')
    
    return HttpResponse('erro, requisicao deve ser POST\r\n')

def logout(request):
    if request.method == 'GET':
        django_logout(request)
        print("logout")
    return render(request, 'logout.html')


