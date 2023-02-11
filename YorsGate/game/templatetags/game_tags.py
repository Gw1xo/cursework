from django import template
from game.models import *

register = template.Library()


@register.simple_tag()
def get_ware():
    return Ware.objects.all()