from django.conf.urls import url
from . import views

app_name = "home"
urlpatterns = [
    url('', views.index, name="index"),
]
