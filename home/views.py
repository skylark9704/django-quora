from django.shortcuts import render
from questions.models import Question, Topic


# Create your views here.
def index(request):
    if request.GET.get('filter'):
        r_topic = Topic.objects.filter(topic=request.GET['filter'])[0]
        latest_question_list = Question.objects.filter(
            topic=r_topic
            ).order_by('-askedOn')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'home/index.html', context)

    else:
        latest_question_list = Question.objects.order_by('-askedOn')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'home/index.html', context)
