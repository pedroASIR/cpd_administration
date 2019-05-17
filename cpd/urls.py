from django.conf.urls import url
from django.urls import path
from cpd.views import first_view


urlpatterns = [
    url(r'^$', first_view, name='first-view'),
]