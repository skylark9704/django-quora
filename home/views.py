from django.shortcuts import render
from questions.models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-askedOn')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'home/index.html', context)
