from django.conf.urls import url
from .views import PageView, PageCreateView

urlpatterns = [
    url(
        regex = r'^create/?$',
        view = PageCreateView.as_view(),
        name='create'
    ),
    url(
        regex = r'^(?P<slug>[^/]+)/?$',
        view = PageView.as_view(),
        name='page'
    ),

]
