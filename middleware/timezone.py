import pytz
from django.utils import timezone

from booking_test.settings import TIME_ZONE


def timezone_middleware(get_response):
    def middleware(request):
        """
        Middleware that activates user's timezone for each request
        """
        if request.user.is_authenticated and hasattr(request.user, "profile"):
            selected_tz = request.user.profile.timezone
        else:
            selected_tz = TIME_ZONE

        timezone.activate(pytz.timezone(selected_tz))

        return get_response(request)

    return middleware
