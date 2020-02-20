from django.conf.urls import url
from . import views

app_name = 'questions'
urlpatterns = [
    url(r'^$', views.index, name="Index"),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name="detailed"),
    url(r'^vote/(?P<question_id>[0-9]+)$', views.vote, name="vote")
]
