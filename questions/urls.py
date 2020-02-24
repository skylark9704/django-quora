from django.conf.urls import url
from questions.views import (QuestionsView, AnswerView, VoteView,
                             QuestionView, TopicView, MyQuestionsView)

app_name = 'questions'
urlpatterns = [
    url(r'^$', QuestionsView.as_view(), name="ask"),
    url(r'^topic/$', TopicView.as_view(), name="topic"),
    url(r'^mine/$', MyQuestionsView.as_view(), name="mine"),
    url(r'^question/(?P<question_id>[0-9]+)/$',
        QuestionView.as_view(), name="detailed"),
    url(r'^vote/(?P<question_id>[0-9]+)$', VoteView.as_view(), name="vote"),
    url(r'^answer/(?P<question_id>[0-9]+)$',
        AnswerView.as_view(), name="answer")
]
