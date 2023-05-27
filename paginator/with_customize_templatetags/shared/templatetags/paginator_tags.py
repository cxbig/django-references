from django import template
from django.core.paginator import Paginator
from django.utils.http import urlencode

register = template.Library()


@register.simple_tag(takes_context=True)
def get_proper_elided_page_range(context, number, on_each_side=2, on_ends=2):
    object_list = context['paginator'].paginator.object_list
    per_page = context['paginator'].paginator.per_page
    paginator = Paginator(object_list, per_page)

    page_range = paginator.get_elided_page_range(number=number, on_each_side=on_each_side, on_ends=on_ends)

    return make_page_range(context, page_range)


@register.simple_tag(takes_context=True)
def render_paginator_url(context, number):
    params = {}
    for key in context['request'].GET:
        params[key] = number if key == 'page' else context['request'].GET[key]
    params['page'] = number
    return '?' + urlencode(params)


def make_page_range(context, page_range):
    result = []
    current_page = context['paginator'].number
    for page_idx in page_range:
        if type(page_idx) == int and page_idx == current_page:
            result.append({
                'is_link': False,
                'text': str(page_idx),
                'li_class': 'page-item active',
            })
        elif type(page_idx) == int:
            result.append({
                'is_link': True,
                'text': str(page_idx),
                'li_class': 'page-item',
                'url': render_paginator_url(context, page_idx)
            })
        else:
            result.append({
                'is_link': False,
                'text': str(page_idx),
                'li_class': 'page-item',
            })

    return result
