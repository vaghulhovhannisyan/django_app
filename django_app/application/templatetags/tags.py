from django import template
from ..models import menu

register = template.Library()


@register.inclusion_tag('range.html')
def template_tag():
    draw_menu = menu.objects.all()
    return {'draw_menu': draw_menu}