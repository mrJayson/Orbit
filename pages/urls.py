from django.conf.urls import url
from .views import PageDetailView, PageCreateView, PageUpdateView, PageHistoryView, PageIndexView

urlpatterns = [
    url(
        regex=r'^create/?$',
        view=PageCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^index/?$',
        view=PageIndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/update/?$',
        view=PageUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/?$',
        view=PageDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/history/?$',
        view=PageHistoryView.as_view(),
        name='history'
    ),
]
