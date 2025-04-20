import json
from django import template

register = template.Library()


@register.filter(name="get_item")
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter(name="get_item_link")
def get_item_link(dictionary, key):
    return dictionary.get(key).get("link") if dictionary.get(key) else None

@register.filter(name="get_item_text")
def get_item_text(dictionary, key):
    return dictionary.get(key).get("text") if dictionary.get(key) else None
