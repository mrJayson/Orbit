from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import PageForm
from .models import Page


class PageDetailView(LoginRequiredMixin, DetailView):
    template_name = 'pages/detail.html'
    model = Page


class PageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pages/form.html'
    model = Page
    form_class = PageForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        if (self.request.method == 'POST'):
            # pass in the author here
            form = form_class(data=self.request.POST, author=self.request.user)
        else:
            form = form_class()
        return form

    def get_success_url(self, **kwargs):
        return reverse('pages:detail', kwargs={'slug': self.object.slug})


class PageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'pages/form.html'
    model = Page
    form_class = PageForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        if (self.request.method == 'POST'):
            form = form_class(author=self.request.user, version=self.object.version, **self.get_form_kwargs())
        else:
            form = super(PageUpdateView, self).get_form(form_class)
        return form

    def get_success_url(self, **kwargs):
        return reverse('pages:detail', kwargs={'slug': self.object.slug})


class PageIndexView(LoginRequiredMixin, ListView):
    template_name = 'pages/index.html'
    model = Page
    queryset = Page.objects.filter(active=True)  # Refers to the 'All' Tab in the index

    def get_context_data(self, *args, **kwargs):
        context = super(PageIndexView, self).get_context_data(*args, **kwargs)
        context['recently_modified'] = Page.objects.filter(active=True).order_by('creation_date')
        return context
