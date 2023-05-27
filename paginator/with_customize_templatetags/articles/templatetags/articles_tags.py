from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_filter_btn_class(context, button_name):
    published = context['request'].GET.get('published', None)
    if published is None:
        if button_name == 'all':
            return 'btn btn-primary'
        else:
            return 'btn btn-outline-primary'
            
    published = str(published).lower() in ('true', 'yes')
    if published and button_name == 'published':
        return 'btn btn-primary'
    if not published and button_name == 'unpublished':
        return 'btn btn-primary'

    return 'btn btn-outline-primary'
