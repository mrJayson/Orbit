from django.conf.urls import url
from .views import EventCreateView, EventDetailView, EventUpdateView, EventIndexView

urlpatterns = [
    url(
        regex=r'^create/?$',
        view=EventCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^index/?$',
        view=EventIndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/update$',
        view=EventUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/?$',
        view=EventDetailView.as_view(),
        name='detail'
    ),
]
