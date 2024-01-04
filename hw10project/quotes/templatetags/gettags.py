from django import template
from django.db.models import Count

from ..models import Tag

register = template.Library()


@register.simple_tag
def get_top_tags():
    tags = Tag.objects.annotate(quote_count=Count('quote')).order_by('-quote_count')
    top_tags = tags[:10]
    sizes = range(35, 0, -3)
    top_tags = [{'tag': tag, 'size': size} for tag, size in zip(top_tags, sizes)]
    return top_tags
