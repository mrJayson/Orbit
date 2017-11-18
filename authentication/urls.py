from django.conf.urls import url
from .views import SignInView, SignOutView, SignUpView

urlpatterns = [
    url(
        regex=r'^signin/?$',
        view=SignInView.as_view(),
        name='signin'
    ),
    url(
        regex=r'^signout/?$',
        view=SignOutView.as_view(),
        name='signout'
    ),
    url(
        regex=r'^signup/?$',
        view=SignUpView.as_view(),
        name='signup'
    ),
]
