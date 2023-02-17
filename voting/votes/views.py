from django.shortcuts import render
from . models import Question, Choice
# Create your views here.

def index(request):
    return render(request, 'votes/index.html')


