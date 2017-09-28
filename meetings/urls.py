from django.conf.urls import url
from .views import MeetingCreateView, MeetingDetailView, MeetingEditView, MeetingIndexView

urlpatterns = [
    url(
        regex=r'^create/?$',
        view=MeetingCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^index/?$',
        view=MeetingIndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/edit$',
        view=MeetingEditView.as_view(),
        name='edit'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/?$',
        view=MeetingDetailView.as_view(),
        name='detail'
    ),
]
