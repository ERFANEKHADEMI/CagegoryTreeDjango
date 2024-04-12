from django import template
from base.models import TreeCategory
from django.db.models.query import QuerySet

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    print(menu_name)
    categories = TreeCategory.objects.prefetch_related("children").filter(parent=None)

    html = "<ul>"
    html += renderList(categories, menu_name)
    html += "</ul>"

    return html


def renderList(categories, menu_name):
    html = ""
    for cat in categories:
        html += f"<li><a href='{createURL(cat)}'>" + cat.name + "</a>"
        if cat.name in menu_name or cat.named_url and cat.named_url in menu_name:
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
    category_url = category.named_url if category.named_url else category.name
    list.append(category_url)
    if category.parent:
        parentProcessing(category.parent, list)

    return list
    