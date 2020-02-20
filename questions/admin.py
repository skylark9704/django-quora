from django.contrib import admin

# Register your models here.
from .models import Question, Vote, Answer

admin.site.register(Question)
admin.site.register(Vote)
admin.site.register(Answer)