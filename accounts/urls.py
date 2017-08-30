from django.conf.urls import url
from .views import AccountDetailView, AccountEditView

urlpatterns = [
    # SignIn url is in urlsignin.py since that lives under a different namespace
    url(
        regex = r'^[A-Za-z0-9]+$',
        view = AccountDetailView.as_view(),
        name='detail'
    ),
    url(
        regex = r'^[A-Za-z0-9]+/edit$',
        view = AccountDetailView.as_view(),
        name='edit'
    ),
]