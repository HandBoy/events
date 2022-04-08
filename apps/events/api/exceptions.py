from django.utils.translation import gettext as _
from rest_framework.exceptions import APIException


class EventssApiException(APIException):
    status_code = 400
    default_detail = _("Api error.")
    default_code = _("sales_api_error")


class ApplicationNotFoundError(EventssApiException):
    """
    Custom API exception for Application not found.
    """
    default_detail = _("Application not found.")
    default_code = _("filter_required")

    def __init__(self, message=None):
        if message:
            self.default_detail = message

        super().__init__()
