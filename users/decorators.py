from django.contrib import messages
from functools import wraps

from django.shortcuts import redirect


def clear_messages(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        storage = messages.get_messages(request)
        for _ in storage:
            pass  # Iterate through and consume existing messages
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def anonymous_required(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Change 'home' to the name of your home page URL
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function
