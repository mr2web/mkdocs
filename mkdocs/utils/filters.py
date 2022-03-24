import jinja2

from mkdocs.utils import normalize_url


@jinja2.pass_context
def url_filter(context, value):
    """ A Template filter to normalize URLs. """
    return normalize_url(value, page=context['page'], base=context['base_url'])
