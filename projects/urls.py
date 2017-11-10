from django.conf.urls import url
from .views import (
    ProjectCreateView,
    ProjectDetailView,
    ProjectIndexView,
)

urlpatterns = [
    url(
        regex=r'^create/?$',
        view=ProjectCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^index/?$',
        view=ProjectIndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/?$',
        view=ProjectDetailView.as_view(),
        name='detail'
    ),
]
