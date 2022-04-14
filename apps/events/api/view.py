from rest_framework import mixins, viewsets

from ..models import Application, Event
from .exceptions import UntrustedApplicationApiError
from .serializers import EventsSerializer


class EventsView(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    View to save a event.
    """
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = []

    def perform_create(self, serializer):
        # TODO overwrite create and add async process to save the event
        # TODO Try get the application with a middleware
        try:
            application = Application.objects.get(
                uuid=self.request.headers.get("Application")
            )
        except Application.DoesNotExist as err:
            raise UntrustedApplicationApiError()

        serializer.validated_data['application'] = application
        super().perform_create(serializer)
