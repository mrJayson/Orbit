from django.conf.urls import url
from .views import PageDetailView, PageCreateView, PageEditView, PageIndexView

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
        regex=r'^(?P<slug>[^/]+)/edit$',
        view=PageEditView.as_view(),
        name='edit'
    ),
    url(
        regex=r'^(?P<slug>[^/]+)/?$',
        view=PageDetailView.as_view(),
        name='detail'
    ),

]
