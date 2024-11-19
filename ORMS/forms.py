#formulario
from django import forms 
from .models import Topic, Entry, Produto, MeuModelo, SalaUps #Saida ItemSaida#importacao das clases de models.py
#Aqui vc cria as classes do formulario
class TopicForm(forms.ModelForm): #cria classe TopicForm, herda de classe model
    class Meta: #cria classe meta
        model = Topic 
        fields = ['text', 'endereco', 'cnpj', 'telefone']
        labels = {'text': ''}#campo vazio para prenchimento do formulario
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['imagem', 'categoria', 'marca', 'nome', 'modelo', 'codigo', 'existente', 'sku', 'preco', 'quantidade']


class MeuModeloForm(forms.ModelForm):
    class Meta:
        model = MeuModelo
        fields = ['nome', 'descricao', 'imagem']

class SalaUpsForm(forms.ModelForm):
    class Meta:
        model = SalaUps
        fields = [ 'sala', 'nome_ds', 'potencia_ds','imagem_ds', 'energia_ete', 'imagem_ete', 'energia_portaria', 'imagem_portaria', 'ups1', 'potencia_ups1', 'imagem_ups1', 'cod1', 'energia_cod1', 'imagem_cod1', 'imagem_cod1z', 'ups2', 'potencia_ups2', 'imagem_ups2', 'cod2', 'energia_cod2', 'imagem_cod2', 'imagem_cod2z' , 'observacao', 'nome_tecnico', 'data_hora']
        labels = {
            'sala': 'SALA','nome_ds': 'Nome DS',
            'potencia_ds': 'Potência DS',
            'imagem_ds': 'Imagem DS',
            'energia_ete': 'Energia ETE', 'imagem_ete': 'Imagem ETE', 'energia_portaria': 'Energia Portaria', 'imagem_portaria': 'Imagem Portaria', 'ups1': 'UPS1', 'potencia_ups1': 'Potência UPS1', 'imagem_ups1': 'Imagem UPS1', 'cod1': 'COD1', 'energia_cod1' : 'Energia COD1', 'imagem_cod1': 'Imagem COD1','imagem_cod1z': 'imagem COD1 Zerado', 'ups2' : 'UPS2', 'potencia_ups2': 'Potência UPS2', 'imagem_ups2': 'Imagem UPS2', 'cod2': 'COD2', 'energia_cod2' : 'Energia COD2', 'imagem_cod2': 'Imagem COD2','imagem_cod2z': 'imagem COD2 Zerado',


        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tornar os campos específicos não obrigatórios
        self.fields['potencia_ds'].required = False
        self.fields['energia_ete'].required = False
        self.fields['imagem_ete'].required = False
        self.fields['energia_portaria'].required = False
        self.fields['imagem_portaria'].required = False
        self.fields['ups1'].required = False
        self.fields['potencia_ups1'].required = False
        self.fields['imagem_ups1'].required = False
        self.fields['ups2'].required = False
        self.fields['potencia_ups2'].required = False
        self.fields['imagem_ups2'].required = False  
     # Defina as opções para o campo de seleção
    OPÇÕES = [
        ('opcao1', 'MS-A'),
        ('opcao2', 'MS-B'),
        ('opcao3', 'GEN'),
        ('opcao4', 'GEN-R'),
    ]
    
    # Campo de seleção (dropdown)
    meu_campo_select = forms.ChoiceField(choices=OPÇÕES, label="Escolha uma opção")
#class 

#class SaidaForm(forms.ModelForm):
    #class Meta:
        #model = Saida
        #fields = ['observacao']

    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        # Adicionar um campo de seleção para os itens da saída
        #produtos_disponiveis = Produto.objects.filter(existente=True, quantidade__gt=0)
        #for produto in produtos_disponiveis:
            #self.fields[f'produto_{produto.id}'] = forms.IntegerField(
                #label=f'{produto.nome} - Modelo: {produto.modelo} - Codigo: {produto.codigo}',  # Combine nome e modelo
                #min_value=0,
                #max_value=produto.quantidade,
                #required=False,
                #initial=0,
            #)

    #def save(self, commit=True):
        #instance = super().save(commit=False)

        # Salvar a instância principal de saída primeiro, se commit=False
        #if not commit:
            #instance.save()

        # Salvar os itens de saída
        #for field_name, field_value in self.cleaned_data.items():
            #if field_name.startswith('produto_') and field_value > 0:
                #produto_id = int(field_name.replace('produto_', ''))
                #produto = Produto.objects.get(pk=produto_id)
                #quantidade = field_value

                # Criar ou atualizar o item de saída
                #ItemSaida.objects.update_or_create(
                    #saida=instance,
                    #produto=produto,
                    #defaults={'quantidade': quantidade}
                #)

        # Agora salvar a instância principal de saída, se commit=True
        #if commit:
            #instance.save()

        #return instance

#class ItemSaidaForm(forms.ModelForm):
    #class Meta:
        #model = ItemSaida
        #fields = ['produto', 'quantidade', 'preco_unitario']




class ProdutoSearchForm(forms.Form):
    query = forms.CharField(label='Buscar produtos', max_length=100)#buscar apenas produtos
    categoria = forms.CharField(label='Categoria', required=False, max_length=100)
    marca = forms.CharField(label='Marca', required=False, max_length=100)
    nome = forms.CharField(label='Nome', required=False, max_length=100)
    modelo = forms.CharField(label='Modelo', required=False, max_length=100)
    codigo = forms.CharField(label='Código', required=False, max_length=100)
    sku = forms.CharField(label='SKU', required=False, max_length=100)
    preco_min = forms.DecimalField(label='Preço Mínimo', required=False, decimal_places=2, max_digits=10)
    preco_max = forms.DecimalField(label='Preço Máximo', required=False, decimal_places=2, max_digits=10)