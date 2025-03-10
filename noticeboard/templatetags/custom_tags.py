# filepath: /Users/vikimulhall/Documents/community/noticeboard/
# templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter(name='is_facilitator')
def is_facilitator(user):
    return user.groups.filter(name="Facilitators").exists()