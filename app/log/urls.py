from django.conf.urls import url

from .views import LogView

urlpatterns = [
    url(r'^machine/(?P<pk>[0-9a-z-]+)/$', LogView.as_view()),
]