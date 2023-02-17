from django.shortcuts import render
from . models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = { 'latest_question_list' : latest_question_list}
    return render(request, 'votes/index.html', context)


