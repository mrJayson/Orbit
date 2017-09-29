from django import template
from django.utils.timesince import timesince, timeuntil
from django.utils.translation import ugettext
from django.utils.html import avoid_wrapping

register = template.Library()


@register.filter(name="timediff", is_safe=False)
def timediff_filter(value, arg=None):
    """Combines the functionality of timesince and timeuntil"""
    if not value:
        return ''
    try:
        if timesince(value, arg) == avoid_wrapping(ugettext('0 minutes')):
            return 'In ' + timeuntil(value, arg)
        else:
            return timesince(value, arg) + ' ago'
    except (ValueError, TypeError):
        return ''
