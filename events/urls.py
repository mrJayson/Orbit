from django.conf.urls import url
from .views import EventCreateView, EventDetailView, EventEditView, EventIndexView

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
        regex=r'^(?P<slug>[^/]+)/edit$',
        view=EventEditView.as_view(),
        name='edit'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/?$',
        view=EventDetailView.as_view(),
        name='detail'
    ),
]
