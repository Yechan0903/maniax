from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

def login_required(function=None, redirect_field_name='next', login_url=None):
    if login_url is None:
        login_url = settings.LOGIN_URL
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
