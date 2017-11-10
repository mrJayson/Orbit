from django import template
from events.models import Event
from pages.models import Page
from projects.models import Project

register = template.Library()


@register.filter(name="label", is_safe=False)
def category_label(page):
    if type(page) == Event:
        return "label-warning"
    if type(page) == Page:
        return "label-primary"
    if type(page) == Project:
        return "label-danger"
    else:
        return "label-default"
