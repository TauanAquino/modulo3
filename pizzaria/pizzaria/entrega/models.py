# coding: utf-8

from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=128, db_index=True)
    fone = models.CharField(max_length=16, db_index=True)
    ramal = models.CharField(max_length=4, blank=True)
    email = models.EmailField(blank=True)
    logradouro = models.CharField(max_length=64, db_index=True)
    numero = models.PositiveIntegerField(verbose_name=u'nº')
    complemento = models.CharField(max_length=32, blank=True)
    obs = models.TextField(verbose_name=u'observação', blank=True)
    
    class Meta:
        ordering = ['fone']
        unique_together = ('fone','ramal')
        db_table = 'pedidos_cliente'
    
    def __unicode__(self):
        if self.ramal:
            return self.fone + ' - ' + self.nome + ' r. ' + self.ramal
        else:
            return self.fone + ' - ' + self.nome
    
    def endereco(self):
        if self.complemento:
            return u'%s, %s - %s' % (self.logradouro, self.numero, self.complemento)
        else:
            return u'%s, %s' % (self.logradouro, self.numero)
        
    def tel_com_ddd(self):
        return u'(12) %s' % self.fone
        
    endereco.short_description = u'Endereço'
    tel_com_ddd.short_description = u'Telefone'
    
class Pedido(models.Model):
    inclusao = models.DateTimeField(auto_now_add = True)
    cliente = models.ForeignKey(Cliente)
    pronto = models.BooleanField(default = False)
    entregador = models.ForeignKey('Entregador', null = True, blank = True)
    partida = models.TimeField(null=True, blank = True)
    
    def __unicode__(self):
        return '%s - %s' % (self.inclusao.strftime('%H:%M:%S'), self.cliente.nome)
    
class Entregador(models.Model):
    nome = models.CharField(max_length=64)
    
    class Meta:
        verbose_name_plural = u'Entregadores'
    
    def __unicode__(self):
        return self.nome

SABORES = [('mussarela', 'Mussarela'),
           ('calabresa', 'Calabresa'),
           ('portuguesa', 'Portuguesa'),
           ('atum', 'Atum'), 
            ]

class Pizza(models.Model):
    pedido = models.ForeignKey(Pedido)
    sabor1 = models.CharField(u'sabor 1', max_length = 32, choices=SABORES)
    coberto1 = models.BooleanField(u'cob.')
    sabor2 = models.CharField(u'sabor 2', max_length = 32, choices=SABORES, blank=True)
    coberto2 = models.BooleanField(u'cob.')
    obs = models.TextField(blank=True)
    
    def __unicode__(self):
        sabor = self.sabor1
        if self.coberto1:
            sabor += '  coberta'
        if self.sabor2:
            sabor2 = self.sabor2
            if self.coberto2:
                sabor2 += '  coberta'
            sabor = u'½ %s, ½ %s' % (sabor, sabor2)
        return sabor
