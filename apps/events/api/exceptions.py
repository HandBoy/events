from django.utils.translation import gettext as _
from rest_framework.exceptions import APIException


class EventssApiException(APIException):
    status_code = 400
    default_detail = _("Api error.")
    default_code = _("sales_api_error")


class UntrustedApplicationApiError(EventssApiException):
    """
    Custom API exception for Untrusted Application.
    """
    default_detail = _("Untrusted Application.")
    default_code = _("untrusted application")

    def __init__(self, message=None):
        if message:
            self.default_detail = message

        super().__init__()
