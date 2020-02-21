from django.conf.urls import url
from . import views

app_name = 'questions'
urlpatterns = [
    url(r'^ask/$', views.ask, name="ask"),
    url(r'^topic/$', views.topic, name="topic"),
    url(r'^topic/add$', views.topic, name="add_topic"),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name="detailed"),
    url(r'^vote/(?P<question_id>[0-9]+)$', views.vote, name="vote"),
    url(r'^answer/(?P<question_id>[0-9]+)$', views.answer, name="answer"),
    url(r'^mine/$', views.mine, name="mine"),
]
