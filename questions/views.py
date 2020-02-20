from django.shortcuts import render
from .models import Question, Vote, Answer


# Create your views here.
def index(request):
    return render(request, 'questions/index.html')


def question(request, question_id):
    query = Question.objects.get(pk=question_id)
    question = {'question': query}
    answers = Answer.objects.filter(question=query)
    votes = Vote.objects.filter(question=query)
    up = 0
    down = 0
    for vote in votes:
        if vote.vote:
            up = up + 1
        else:
            down = down + 1
    return render(
        request, 'questions/index.html',
        {
            'question': question,
            'votes': {'up': up, 'down': down},
            'answers': answers
        }
    )


def vote(request, question_id):

    return None
