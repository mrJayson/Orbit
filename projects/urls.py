from django.conf.urls import url
from .views import (
    ProjectIndexView,
)

urlpatterns = [
    url(
        regex=r'^index/?$',
        view=ProjectIndexView.as_view(),
        name='index'
    ),
]
