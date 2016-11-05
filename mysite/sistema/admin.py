from django.contrib import admin
from sistema.models import registro


class registroAdmin(admin.ModelAdmin):
	model = registro
	list_display = ('id','nome' ,'data_nascimento', 'profissão','telefone','cpf',)
	list_filter = ('data_nascimento',)
	

admin.site.register(registro,registroAdmin)



