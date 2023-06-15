from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def sitename():
    return settings.SITE_NAME
    
@register.simple_tag
def baseurl():
    return settings.BASE_URL

@register.filter
def member(obj, name):
    return getattr(obj, name, None)

@register.filter
def class_name(obj):
    return obj.__class__.__name__