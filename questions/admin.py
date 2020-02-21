from django.contrib import admin

# Register your models here.
from .models import Question, Vote, Answer, Topic

admin.site.register(Question)
admin.site.register(Vote)
admin.site.register(Answer)
admin.site.register(Topic)
