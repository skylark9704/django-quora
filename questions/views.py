from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Vote, Answer, Topic
from django.views import View

from django.core import serializers


class QuestionsView(View):
    def get(self, request, question):
        return render(request, 'questions/index.html')

    def post(self, request):
        topic = Topic.objects.get(pk=request.POST['topic'])
        q = Question(
            question_text=request.POST['text'],
            title=request.POST['title'],
            user=request.user,
            topic=topic
        )

        q.save()
        return redirect('/home/')


# Create your views here.
class QuestionView(View):
    def get(self, request, question_id):
        query = Question.objects.get(pk=question_id)
        question = {'question': query}
        answers = Answer.objects.filter(question=query)
        votes = Vote.objects.filter(question=query)
        up = 0
        down = 0
        for vote in votes:
            if vote.vote == 1:
                up = up + 1
            elif vote.vote == -1:
                down = down + 1
        return render(
            request, 'questions/index.html',
            {
                'question': question,
                'votes': {'up': up, 'down': down},
                'answers': answers
            }
        )


class VoteView(View):
    def get(self, request):
        pass

    def post(self, request, question_id):
        q = Question.objects.get(pk=question_id)
        v = get(Vote.objects.filter(user=request.user, question=q), 0)

        if not v:
            vote = Vote(
                question=q,
                vote=request.POST['vote'],
                user=request.user
            )
            vote.save()

        else:
            if not f'{v.vote}' == request.POST['vote']:
                v.vote = request.POST['vote']
                v.save()

        return redirect(f'/questions/question/{question_id}')


class AnswerView(View):
    def post(self, request, question_id):
        q = Question.objects.get(pk=question_id)
        answer = Answer(
            answer=request.POST['answer'],
            user=request.user,
            question=q
        )

        answer.save()
        return redirect(f'/questions/question/{question_id}')


class TopicView(View):
    def get(self, request):
        topics = Topic.objects.all()
        return render(request, 'questions/add_topics.html', {'topics': topics})

    def post(self, request):
        topic = Topic(
            topic=request.POST['topic']
        )

        topic.save()

        return redirect('/questions/topic')


class MyQuestionsView(View):
    def get(self, request):
        questions = Question.objects.filter(user=request.user)
        answers = Answer.objects.filter(user=request.user)
        for row in questions:
            up = 0
            down = 0
            votes = Vote.objects.filter(question=row)
            for vote in votes:
                if vote.vote == 1:
                    up = up + 1
                elif vote.vote == -1:
                    down = down + 1

            row.up = up
            row.down = down
        return render(
            request,
            'questions/my_questions.html',
            {'asked': questions, 'answered': answers}
        )


class SearchView(View):
    def get(self, request):
        questions = Question.objects.filter(
            title__icontains=request.GET.get('query')
        )
        return HttpResponse(
            serializers.serialize('json', questions),
            content_type="application/json"
        )


def get(l, index, default=False):
    try:
        return l[index]
    except IndexError:
        return default
