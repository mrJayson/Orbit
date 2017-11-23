from django.conf.urls import url
from .views import (
    ProjectBoardView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectIndexView,
    ProjectUpdateView,
    TaskCreateView,
    TaskDetailView,
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
        regex=r'^(?P<slug>[^/]+)/task/create/?$',
        view=TaskCreateView.as_view(),
        name='task_create'
    ),
    url(
        regex=r'^(?P<project_slug>[^/]+)/task/(?P<task_slug>[^/]+)/?$',
        view=TaskDetailView.as_view(),
        name='task_detail'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/board/?$',
        view=ProjectBoardView.as_view(),
        name='board'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/update/?$',
        view=ProjectUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/?$',
        view=ProjectDetailView.as_view(),
        name='detail'
    ),
]
