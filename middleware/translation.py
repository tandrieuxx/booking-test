from django.utils import translation

from booking_test.settings import LANGUAGE_CODE


def translation_middleware(get_response):
    def middleware(request):
        """
        Middleware that activates translation according user's language for each request
        """
        if request.user.is_authenticated and hasattr(request.user, "profile"):
            user_language = request.user.profile.language
        else:
            user_language = LANGUAGE_CODE

        translation.activate(user_language)
        request.session[translation.LANGUAGE_SESSION_KEY] = user_language

        return get_response(request)

    return middleware
