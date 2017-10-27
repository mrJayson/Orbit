from django import template
from django.template.loader import render_to_string
from django.utils import six
from avatar.conf import settings
from avatar.templatetags.avatar_tags import avatar_url, has_avatar
from avatar.utils import cache_result
from orbit.settings import NUM_COLOURS
import hashlib

register = template.Library()


@cache_result()
@register.simple_tag
def avatar(user, size=settings.AVATAR_DEFAULT_SIZE, **kwargs):
    if has_avatar(user):
        # Use assigned avatar
        alt = six.text_type(user)
        url = avatar_url(user, size)
        kwargs.update({'alt': alt})
        context = {
            'user': user,
            'url': url,
            'size': size,
            'kwargs': kwargs,
        }
        return render_to_string('avatar/avatar_tag.html', context)
    else:
        # Dynamically generate an avatar based on the user's initials
        letter = '?'
        if user.first_name:
            letter = user.first_name[0].upper()
            if user.last_name:
                letter += user.last_name[0].upper()
        elif user.username:
            letter = user.username[0].upper()

        colour_ix = int(hashlib.md5(str(user.id).encode()).hexdigest(), 16) % NUM_COLOURS
        context = {'colour_ix': colour_ix, 'letter': letter, 'size': size, 'font_size': (size / 2)}
        return render_to_string('accounts/dynamic_avatar.svg', context)
