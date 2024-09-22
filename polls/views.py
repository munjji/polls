from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.

def index(request):
    # Question.objects.all()
    # -를 붙이면 내림차순, 안 붙이면 오름차순
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     q = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question {} does not exist'.format(question_id))
    q = get_object_or_404(Question, id = question_id)

    return render(request, 'polls/detail.html', {'question' : q})


def vote(request, question_id):
    response = "You're voting on the question {}."
    return HttpResponse(response.format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))