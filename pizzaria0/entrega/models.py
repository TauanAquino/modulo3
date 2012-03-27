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
    obs = models.TextField(verbose_name=u'observação')
    
    class Meta:
        ordering = ('nome','fone')
        unique_together = ('fone','ramal')
        db_table = 'pedidos_cliente'
    
    def __unicode__(self):
        return self.nome

