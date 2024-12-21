# your_app/templatetags/form_tags.py
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Adds a CSS class to the form field widget.
    Example: {{ form.field_name|add_class:"form-input" }}
    """
    return value.as_widget(attrs={'class': arg})
