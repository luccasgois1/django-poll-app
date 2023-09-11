from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice


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
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        "polls/results.html",
        {
            "question": question,
        },
    )

def vote(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You did not select a choice.",
            },
        )
    else:
        selected_choice.vote += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
