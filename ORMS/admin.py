from django.contrib import admin
from ORMS.models import Topic, Entry, Produto #importa a class topic no arquivo models
# Register your models here.
admin.site.register(Topic) #cria topicos
admin.site.register(Entry)
admin.site.register(Produto)