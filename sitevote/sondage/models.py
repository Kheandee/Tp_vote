from django.db import models
from django.forms import CharField

# Création des modèles
class LaQuestion(models.Model):
    texte_question = models.CharField(max_length=100)
    date_publication = models.DateTimeField('Date de publication')

class Choix(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # A continuer
    texte_choix =