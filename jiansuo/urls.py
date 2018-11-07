from django.conf.urls import url

from . import view

urlpatterns = [
    url(r'^$', view.index),
    url(r'^index/', view.index),
    url(r'^163/', view.wy_163),
    url(r'^qq/', view.qq),
    url(r'^qqqun/', view.qqqun),
]
