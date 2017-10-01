from django.conf.urls import url
from .views import PageDetailView, PageCreateView, PageUpdateView, PageIndexView

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
        regex=r'^(?P<slug>[^/]+)/update$',
        view=PageUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/?$',
        view=PageDetailView.as_view(),
        name='detail'
    ),

]
