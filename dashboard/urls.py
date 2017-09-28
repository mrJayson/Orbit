from django.conf.urls import url
from .views import DashboardView

urlpatterns = [
    url(
        regex=r'^$',
        view=DashboardView.as_view(),
        name='dashboard'
    )
]
