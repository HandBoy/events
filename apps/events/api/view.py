from rest_framework import mixins, viewsets

from ..models import Application, Event
from .exceptions import ApplicationNotFoundError
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
        try:
            application = Application.objects.get(
                uuid=self.request.headers.get("Application")
            )
        except Application.DoesNotExist as err:
            raise ApplicationNotFoundError()

        serializer.validated_data['application'] = application
        super().perform_create(serializer)
