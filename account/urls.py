from django.conf.urls import url
from . import views

app_name = "account"

urlpatterns = [
    url(r'^login', views.classic_login, name='login'),
    url(r'^logout', views.signout, name='logout'),
    url(r'^google/signin', views.index, name='google'),
    url(r'^oauth/callback', views.oauth, name='oauth'),
    url(r'^profile', views.profile, name="profile")
]
