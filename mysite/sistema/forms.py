from django import forms
from django.contrib.auth.models import User



class registroForm(forms.Form):
	nome = forms.CharField(label='Nome', max_length=200)
	data_nascimento = forms.DateField(label = 'Nascimento')
	profissão = forms.CharField(label = 'Profissão' , max_length=200)
	telefone = forms.IntegerField(label = 'Telefone')
	cpf = forms.IntegerField(label = 'CPF')


class cadastroForm(forms.Form):
	nome = forms.CharField(label= 'usuário', max_length=200,widget=forms.TextInput)
	email = forms.EmailField(label = 'Email' ,  max_length=200)
	senha = forms.CharField(label ='Senha' , max_length=50,widget=forms.PasswordInput(render_value = False))
	confirmar_senha = forms.CharField(label ='Confirmar Senha' , max_length=50,widget=forms.PasswordInput(render_value=False))
    
	
	


