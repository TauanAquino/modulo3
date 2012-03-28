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
        ordering = ('nome','fone')
        unique_together = ('fone','ramal')
        db_table = 'pedidos_cliente'
    
    def __unicode__(self):
        return self.nome
    
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
    
class Entregador(models.Model):
    nome = models.CharField(max_length=64)
    
    class Meta:
        verbose_name_plural = u'Entregadores'
    
    def __unicode__(self):
        return self.nome
