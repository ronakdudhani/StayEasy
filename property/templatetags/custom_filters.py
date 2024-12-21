from django import template

register = template.Library()

@register.filter(name='split')
def split(value, separator=','):
    """Splits a string by the given separator (defaults to comma)."""
    return value.split(separator) if value else []
