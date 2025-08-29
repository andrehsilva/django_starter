# a_core/templatetags/i18n_tags.py

from django import template
from django.urls import resolve, reverse
from django.utils.translation import get_language

register = template.Library()

@register.simple_tag(takes_context=True)
def url_without_lang(context):
    """
    Returns the absolute path of the current page without the language prefix.
    """
    request = context['request']
    resolver_match = request.resolver_match
    
    # Reconstruct the URL without the language prefix
    # This is more robust as it uses URL names instead of string manipulation
    try:
        url = reverse(
            resolver_match.view_name,
            args=resolver_match.args,
            kwargs=resolver_match.kwargs,
            current_app=resolver_match.app_name
        )
        if request.GET:
            url += '?' + request.GET.urlencode()
        return url
    except:
        # Fallback for URLs without a name
        return request.get_full_path()