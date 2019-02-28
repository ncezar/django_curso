from django.db import models
from django import forms

# Create your models here.
class Usuario(models.Model):
    usuario= models.CharField(max_length=200)
    senha = models.CharField(max_length=32)
    def __str__(self):
        return str(self.usuario)
