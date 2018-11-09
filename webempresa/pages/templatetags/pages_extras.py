from django import template
from pages.models import Page

register = template.Library()

#Registro en Librería de Templates.
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages