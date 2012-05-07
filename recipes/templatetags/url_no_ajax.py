from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter

def url_no_ajax(text):
    return text.replace('<a ', '<a data-ajax="false" ')
url_no_ajax.is_safe = True
