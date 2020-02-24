from django import forms
from questions.models import Topic


def getChoices():
    query = Topic.objects.all()
    topics = []
    for topic in query:
        topics.extend(topic.topic)

    return topics


class Question(forms.Form):

    title = forms.forms.CharField(help_text='Title')
    text = forms.forms.CharField(help_text='A small description')
    topic = forms.ChoiceField(choices=getChoices(), required=True)
