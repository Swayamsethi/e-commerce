from django import template

register = template.Library()

@register.inclusion_tag('messages.html')
def show_messages():
    return {}