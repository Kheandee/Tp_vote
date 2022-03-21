from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    texte_question = models.CharField(max_length=200)
    date_publication = models.DateTimeField('Date de publication')

    def __str__(self):
        return self.texte_question
    
    def publie_recemment(self):
        return self.date_publication >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    texte_choix = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.texte_choix