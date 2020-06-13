from django import template
from blog.models import Category
from django.template import Context

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html', takes_context=True)
def show_menu(context, menu_class='menu'):
    categories = Category.objects.all()
    current_path = context['request'].get_full_path()
    return {'categories': categories, 'menu_class': menu_class, 'current_path': current_path}
