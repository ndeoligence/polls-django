from django.shortcuts import render
from django.http import HttpResponse
from .models import Choice, Question


def index(request):
    return HttpResponse('<h2>Polls home page</h2><br/>')


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
