import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Topic(models.Model):
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.topic


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    question_text = models.CharField(max_length=500)
    askedOn = models.DateTimeField('date published', default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def was_published_recently(self):
        return self.askedOn >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    createdOn = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.answer


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return f'self.vote'
