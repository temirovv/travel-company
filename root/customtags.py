import warnings
from django.template.library import Library

register = Library()


class RemovedInDjango51Warning(PendingDeprecationWarning):
    pass


@register.filter(is_safe=False)
def length_is(value, arg):
    """Return a boolean of whether the value's length is the argument."""
    warnings.warn(
        "The length_is template filter is deprecated in favor of the length template "
        "filter and the == operator within an {% if %} tag.",
        RemovedInDjango51Warning,
    )
    try:
        return len(value) == int(arg)
    except (ValueError, TypeError):
        return ""
