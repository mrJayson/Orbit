from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from .forms import PageCreateForm
from .models import Page

class PageView(LoginRequiredMixin, DetailView):
    template_name = 'pages/page.html'
    model = Page

class PageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pages/page_create.html'
    form_class = PageCreateForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        if (self.request.method == 'POST'):
            # pass in the author here
            form = form_class(self.request.user, self.request.POST)
        else:
            form = form_class()
        return form

    def get_success_url(self, **kwargs):
        return reverse('pages:page', kwargs={'slug': self.object.slug})

class PageIndexView(LoginRequiredMixin, ListView):
    template_name = 'pages/page_index.html'
    model = Page
