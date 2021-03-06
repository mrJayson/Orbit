"""orbit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render
from avatar import urls as avatar

local_patterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^', include('authentication.urls', namespace='authentication')),
    url(r'^', include('dashboard.urls', namespace='dashboard')),
    url(r'^event/', include('events.urls', namespace='events')),
    url(r'^page/', include('pages.urls', namespace='pages')),
    url(r'^project/', include('projects.urls', namespace='projects')),
]

third_party_patterns = [
    url(r'^avatar/', include(avatar)),
]

urlpatterns = local_patterns + third_party_patterns


def fourohfour(request):
    return render(request, '404.html', status=404)


handler404 = fourohfour
