from django.conf.urls import url
from .views import AccountDetailView, AccountUpdateView


urlpatterns = [
    url(
        regex=r'^(?P<pk>[^/]+)/?$',
        view=AccountDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/edit/?$',
        view=AccountUpdateView.as_view(),
        name='edit'
    ),
]
