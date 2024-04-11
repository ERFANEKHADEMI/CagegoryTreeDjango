from django import template
from base.models import TreeCategory
from django.db.models.query import QuerySet

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    parent_categories, categories = TreeCategory.objects.filter(name=menu_name), []

    if len(parent_categories) > 0:
        for parent_category in parent_categories:
            categories = TreeCategory.objects.filter(parent=parent_category)
    else:
        categories = TreeCategory.objects.all()

    html = "<ul>"

    for category in categories:
        if isinstance(category, QuerySet):
            html += '<li>'
            html += renderList(category)
            html += '</li>'
        else:
            html += f"<li><a href='/{menu_name}-{category.name}'>{category.name}</a></li>"

    html += "</ul>"

    return html


def renderList(categories):
    if isinstance(categories, QuerySet):
        print("LIST: ", categories)
        for i in categories:
            renderList(i)
    else:
        return categories.name
