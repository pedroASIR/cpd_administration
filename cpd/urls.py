from django.conf.urls import url
from django.urls import path
from cpd.views import insert_database, index_view, incidencias_view

urlpatterns = [
    url(r'^$', index_view, name='index-view'),
    url(r'^incidencias/$', incidencias_view, name='incidencias-view'),
    url(r'^post/', insert_database, name='insert-database'),
]