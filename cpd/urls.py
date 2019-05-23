from django.conf.urls import url
from django.urls import path
from cpd.views import sensor_list_view, sensor_detail_view, insert_database

urlpatterns = [
    url(r'^lista/$', sensor_list_view, name='sensor-list-view'),
    url(r'^detail/(?P<pk>\d+)$', sensor_detail_view, name='sensor-detail-view'),
    url(r'^post/', insert_database, name='insert-database'),
]