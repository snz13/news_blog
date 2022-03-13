from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
