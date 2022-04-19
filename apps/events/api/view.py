from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Application, Event
from .exceptions import UntrustedApplicationApiError
from .serializers import EventsSerializer


class EventsView(
    CreateAPIView,
    GenericViewSet,
):
    """
    View to save a event.
    """
    # TODO overwrite create and add async process to save the event
    # TODO Try get the application with a middleware
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        application = self.get_application()

        events = [Event(application=application, **e) for e in serializer.validated_data]
        Event.objects.bulk_create(events)
        
        return Response([], status=status.HTTP_201_CREATED)

    def get_application(self):
        try:
            return Application.objects.get(
                uuid=self.request.headers.get("Application")
            )
        except Application.DoesNotExist as err:
            raise UntrustedApplicationApiError()
