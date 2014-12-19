from django import template
from taggit.models import Tag

from ..models import Entry

register = template.Library()

@register.inclusion_tag('blog/_entry_history.html')
def entry_history():
    entries = Entry.objects.order_by('-created_at')[:6]
    return {'entries': entries}

@register.inclusion_tag('blog/_tag_list.html')
def tag_list():
    tags = Tag.objects.order_by('name')
    return {'tags': tags}
