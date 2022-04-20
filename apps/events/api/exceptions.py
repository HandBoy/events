from django.utils.translation import gettext as _
from rest_framework.exceptions import APIException


class EventsApiException(APIException):
    status_code = 400
    default_detail = _("Api error.")
    default_code = _("events_api_error")


class UntrustedApplicationApiError(EventsApiException):
    """
    Custom API exception for Untrusted Application.
    """
    default_detail = _("Untrusted Application.")
    default_code = _("untrusted application")

    def __init__(self, message=None):
        if message:
            self.default_detail = message

        super().__init__()


class CategoryNotFoundApiError(EventsApiException):
    """
    Custom API exception for category not found.
    """
    default_detail = _("Category not found.")
    default_code = _("category_not_found")

    def __init__(self, message=None):
        if message:
            self.default_detail = message

        super().__init__()


class CategoryWithoutStandardApiError(EventsApiException):
    """
    Custom API exception for category without standard.
    """
    default_detail = _("Category without standard. Please use: 'category name'")
    default_code = _("category_without_standard")

    def __init__(self, message=None):
        if message:
            self.default_detail = message

        super().__init__()
