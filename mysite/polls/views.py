from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    
    context = {"latest_question_list": latest_questions_list,}
    template = "polls/index.html"
    return render(request, template, context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    context = {"question": question}
    template = "polls/detail.html"
    return render(request, template, context)

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    response = f"You're voting on question {question_id}"
    return HttpResponse(response)