# coding: utf-8

from django.contrib import admin
from django.forms import Textarea
from django.db.models import TextField
from models import Cliente, Pedido, Entregador, Pizza

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'tel_com_ddd')
    list_display_links = list_display
    search_fields = ['fone','nome','logradouro']
    list_filter = ('logradouro',)

class PizzaAdmin(admin.TabularInline):
    model = Pizza
    extra = 1
    formfield_overrides = {
                    TextField: {'widget': Textarea(attrs={'rows':2, 'cols':50})}
                           }
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('hora_inclusao', 'cliente', 'pronto', 'partiu')
    list_display_links = list_display
    list_filter = ('pronto',)
    date_hierarchy = 'inclusao'
    
    def hora_inclusao(self, obj):
        return obj.inclusao.strftime('%H:%M:%S')
    
    def partiu(self, obj):
        return bool(obj.pronto and obj.entregador and obj.partida)
    partiu.boolean = True
    
    inlines = [PizzaAdmin]
    list_select_related = True

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Entregador)

