from account.models import Auth
from questions.models import Topic


def extra(request):
    if not request.user.is_anonymous:
        auth = Auth.objects.filter(user=request.user)
        if not auth:
            return {'auth': None}
        return {'auth': auth[0]}
    else:
        return {'auth': None}


def topics(request):
    topic = Topic.objects.all()
    return {'topics': topic}
