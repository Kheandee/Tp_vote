from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    return render(request, 'sondage/index.html')

def detail(request, question_id):
    return HttpResponse("Choix numéro %s" % question_id)

def results(request, question_id):
    reponse = "Votes de la question numéro %s."
    return HttpResponse(reponse % question_id)

def vote(request, question_id):
    return HttpResponse("Vous votez pour la question numéro %s." % question_id)