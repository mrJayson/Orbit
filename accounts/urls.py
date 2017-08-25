from django.conf.urls import url
from .views import AccountDetailView, AccountEditView, SignInView, SignOutView, SignUpView

urlpatterns = [
    url(
        regex = r'^[A-Za-z0-9]+$',
        view = AccountDetailView.as_view(),
        name='account_detail'
    ),
    url(
        regex = r'^[A-Za-z0-9]+/edit$',
        view = AccountDetailView.as_view(),
        name='account_edit'
    ),
    url(
        regex = r'^sign_in/$',
        view = SignInView.as_view(),
        name='account_sign_in'
    ),
    url(
        regex = r'^sign_out/$',
        view = SignOutView.as_view(),
        name='account_sign_out'
    ),
    url(
        regex = r'^sign_up/$',
        view = SignUpView.as_view(),
        name='account_sign_up'
    ),
]
