from django import template
from django.urls import resolve

register = template.Library()





@register.filter
def is_active(request, view_name) -> bool:
    current_view = resolve(request.path_info).view_name
    if current_view == view_name:
        return True
    return False
