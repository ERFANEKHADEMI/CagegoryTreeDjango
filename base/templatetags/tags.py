from django import template
from base.models import TreeCategory
from django.db.models.query import QuerySet

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_elements = menu_name.split('::')[-1]
    categories = TreeCategory.objects.prefetch_related("children").filter(parent=None)

    html = "<ul>"
    html += renderList(categories, menu_name)
    html += "</ul>"

    return html


def renderList(categories, menu_name):
    html = ""
    for cat in categories:
        html += f"<li><a href='{createURL(cat)}'>" + cat.name + "</a>"
        if cat.name in menu_name:
            html += "<span>- развернуто</span>"
            html += "</li>"
            if cat.children.count() > 0:
                html += "<ul>"
                html += renderList(cat.children.all(), menu_name)
                html += "</ul>"

    return html

def createURL(category):
    url, list = "", []

    list = parentProcessing(category, list)
    list.reverse()

    for i in list:
        url += f"/{i}"

    return url

def parentProcessing(category, list):
    list.append(category.name)
    if category.parent:
        parentProcessing(category.parent, list)

    return list
    