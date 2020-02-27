from django.conf.urls import url
from .views import Authentication, Account

app_name = "account"

urlpatterns = [
    url(r'^auth/(?P<slug>.+)/$', Authentication.as_view(), name='account'),
    url(r'^oauth/(?P<slug>.+)/$', Authentication.as_view(), name="oauth"),
    url(r'^profile/(?P<slug>.*)/$', Account.as_view(), name="profile"),
]
