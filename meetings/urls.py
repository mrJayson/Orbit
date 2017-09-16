from django.conf.urls import url
from .views import MeetingCreateView, MeetingIndexView

urlpatterns = [
    url(
        regex = r'^index/?$',
        view = MeetingIndexView.as_view(),
        name='index'
    ),
    url(
        regex = r'^create/?$',
        view = MeetingCreateView.as_view(),
        name='create'
    ),

]
