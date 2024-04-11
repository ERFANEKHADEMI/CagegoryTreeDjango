from django import template
from base.models import TreeCategory
from django.db.models.query import QuerySet

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_last_element = menu_name.split('::')[-1]
    parent_categories, categories = TreeCategory.objects.filter(name=menu_last_element), []

    # if len(parent_categories) == 0:
        # parent_categories = TreeCategory.objects.filter(named_url=menu_last_element)

    if len(parent_categories) > 0:
        for parent_category in parent_categories:
            categories = TreeCategory.objects.filter(parent=parent_category)
    else:
        categories = TreeCategory.objects.all()

    html = f"<a href='/{menu_name}'>{ menu_last_element }</a>"
    html += "<ul>"

    for category in categories:
        if isinstance(category, QuerySet):
            html += '<li>'
            html += renderList(category)
            html += '</li>'
        else:
            html += ("<li>" +
                        "<a " +
                            f"href='/{menu_name}::{category.named_url if category.named_url else category.name}'>" +
                                f"{category.name}" +
                        "</a>" +
                     "</li>")

    html += "</ul>"

    return html


def renderList(categories):
    if isinstance(categories, QuerySet):
        print("LIST: ", categories)
        for i in categories:
            renderList(i)
    else:
        return categories.name
