import pytz
from django.utils import timezone

from booking_test.settings import TIME_ZONE


def timezone_middleware(get_response):
    def middleware(request):
        """
        Middleware that activates user's timezone for each request
        """
        if request.user.is_authenticated and hasattr(request.user, "profile"):
            request.timezone = request.user.profile.timezone
        else:
            request.timezone = TIME_ZONE

        timezone.activate(pytz.timezone(request.timezone))

        return get_response(request)

    return middleware
