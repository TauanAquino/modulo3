# coding: utf-8

from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    fone = models.CharField(max_length=16)
    email = models.EmailField(blank=True)
    
    class Meta:
        db_table = 'pedidos_cliente'
    
    def __unicode__(self):
        return self.nome

