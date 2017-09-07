from django.conf.urls import url
from .views import PageView, PageCreateView, PageIndexView

urlpatterns = [
    url(
        regex = r'^create/?$',
        view = PageCreateView.as_view(),
        name='create'
    ),
    url(
        regex = r'^index/?$',
        view = PageIndexView.as_view(),
        name='index'
    ),
    url(
        regex = r'^(?P<slug>[^/]+)/?$',
        view = PageView.as_view(),
        name='page'
    ),

]
