from django import template
from ..models import menu
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def draw_menu(title_menu):
    items = menu.objects.filter(name=title_menu)
    return mark_safe(template_tag(items))

def template_tag(items):
    template = '<ul>'
    for item in items:
        template += '<li>'
        if item.url:
            template += f'<a href="{item.url}">{item.name}</a>'
        else:
            template += item.name
        if item.children.exists():
            template += template_tag(item.children.all())
        template += '</li>'
    template += '</ul>'
    return template

