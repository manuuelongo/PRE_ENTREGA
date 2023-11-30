from typing import Any
from django.db import models
from django.db.models.fields import CharField, DateField
from django.core.validators import MaxValueValidator
from django import forms

class Game(models.Model):
    CONSOLE_CHOICES = [
        ('Xbox', 'Xbox'),
        ('PC', 'PC'),
        ('Nintendo Switch', 'Nintendo Switch'),
        ('PS5', 'PS5'),
        ('Sin Información', 'Sin Información')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=350)
    console = models.CharField(max_length=20, choices=CONSOLE_CHOICES)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Opinion(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    opinion = models.TextField(max_length=300, null=True, blank=True)

class Comentario(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    autor_name = models.CharField(max_length=100)
    comentario = models.CharField(max_length=150)
    date = models.DateField()

 
