from django.conf.urls import url
from . import views

app_name = "account"

urlpatterns = [
    url(r'^logout', views.signout, name='logout'),
    url(r'^google/signin', views.index, name='google'),
    url(r'^oauth/callback', views.oauth, name='oauth')
]
