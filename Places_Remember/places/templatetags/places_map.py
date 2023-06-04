from django import template
from places.models import memories

register = template.Library()

@register.simple_tag()
def get_memories(filter=None):
    if not filter:
        return None
    else:
        return memories.objects.filter(useruid=filter)