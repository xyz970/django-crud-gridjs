from django import template
from django.shortcuts import redirect, reverse

register = template.Library()


class HelperTag:
    pass


@register.simple_tag(name='get_url_path')
def get_url(url_name, **kwargs):
    return reverse(url_name, kwargs=kwargs)



# register.filter('get_url', get_url)
# register.
