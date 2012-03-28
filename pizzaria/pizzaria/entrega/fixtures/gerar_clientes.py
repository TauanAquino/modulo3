# coding: utf-8

qty_clientes_to_generate = 20

''' 
[
  {
    "pk": , 
    "model": "entrega.cliente", 
    "fields": {
      "ramal": "", 
      "complemento": "", 
      "nome": "", 
      "fone": "", 
      "logradouro": "", 
      "numero": , 
      "obs": "", 
      "email": ""
    }
  }
]
'''

from random import randint, choice

LOGRADOUROS = ['Rua Girassol','Rua Giralua', 'Rua Giraterra', 'Rua Giramarte']

registers = []
for i in range(qty_clientes_to_generate):
    campos = dict(ramal = '', complemento = '', obs = '', email = '',
        nome = 'Cliente #%04d' % i, 
        fone = '%4d-%04d' % (randint(3900,3999),randint(0,9999)),
        numero = i + randint(50,1000),
        logradouro = choice(LOGRADOUROS))
    reg = dict(pk=i, model='entrega.cliente',fields=campos)
    registers.append(reg)
   
import json
with open('clientela.json','wb') as arqjson:
    json.dump(registers,arqjson, indent=2)
