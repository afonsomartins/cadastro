from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from sistema.models import registro 
from sistema.models import cadastro
from sistema.forms import registroForm,cadastroForm
from datetime import datetime, timedelta
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

@login_required
def dados(request):
	data = {}
	data['form'] = registroForm
	data['lista_de_pessoas'] = registro.objects.all().order_by('-id')
    
	form = registroForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			nome = form.cleaned_data["nome"]
			data_nascimento = form.cleaned_data["data_nascimento"]
			profissão = form.cleaned_data["profissão"]
			telefone = form.cleaned_data["telefone"]
			cpf = form.cleaned_data["cpf"]
			
			date = registro()
			date.nome = nome
			date.data_nascimento = data_nascimento
			date.profissão = profissão
			date.telefone = telefone
			date.cpf = cpf
			
		
			date.save()
	return render(request, 'dados.html', data)

def do_login(request):
	if request.method == "POST":
		user = authenticate(username = request.POST['username'],password =request.POST['password'] )
		if user is not None :
			login(request , user)
			return redirect('/dados')

	return render(request , 'login.html')

def do_logout(request):
	logout(request)
	return redirect('/login')

def cadastro(request):
        form = cadastroForm(request.POST)
        if request.method == 'POST':
          
            if form.is_valid(): 
               nome = form.cleaned_data['nome']
               email = form.cleaned_data['email']
               senha = form.cleaned_data['senha']
               confirmar_senha = form.cleaned_data['confirmar_senha']
               user = User.objects.create_user(username=nome,email=email,password=senha)
              
               user.save()



        return render(request, "cadastro_feito.html", {"formulario": cadastroForm() })
	