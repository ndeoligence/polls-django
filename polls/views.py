from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Choice, Question


def index(request):
    return render(request, 'polls/index.html', {'questions': Question.objects.order_by('-pub_date')[:5]})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.order_by('votes', 'id')
    ctx = {'question': question, 'choices': choices}
    return render(request, 'polls/detail.html', ctx)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
