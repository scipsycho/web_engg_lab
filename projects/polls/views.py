from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(render(request,'polls/index.html',context))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not Exist")
    return render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
    response = "You are looking at the results of {}".format(question_id)

    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s"% question_id)
