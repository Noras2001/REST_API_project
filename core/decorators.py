# core/decorators.py
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from functools import wraps

def group_required(allowed_groups=[]):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_groups).exists():
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("У вас нет доступа к этой странице.")
        return _wrapped_view
    return decorator


