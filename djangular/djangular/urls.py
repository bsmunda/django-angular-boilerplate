from django.conf.urls import patterns, url, include
from djangular.views import IndexView
from django.conf.urls import url


urlpatterns = [
    url('^.*$', IndexView.as_view(), name='index'),
]
