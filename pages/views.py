from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from .forms import PageForm
from .models import Page

class PageView(LoginRequiredMixin, DetailView):
    template_name = 'pages/page.html'
    model = Page

class PageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pages/page_form.html'
    model = Page
    form_class = PageForm

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

class PageEditView(LoginRequiredMixin, UpdateView):
    template_name = 'pages/page_form.html'
    model = Page
    form_class = PageForm

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


class PageIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PageIndexView, self).get_context_data(*args, **kwargs)
        context['recently_modified'] = Page.objects.order_by('creation_date')[:20]
        return context
