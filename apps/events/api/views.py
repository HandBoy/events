from apps.events.exceptions import (
    AplicationNotFoundUseCase,
    CategoryNotFoundUseCase,
    CategoryWithoutStandardUseCase
)
from apps.events.use_cases import EventUseCase
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Event
from .exceptions import (
    CategoryNotFoundApiError,
    CategoryWithoutStandardApiError,
    UntrustedApplicationApiError
)
from .serializers import EventsSerializer


class EventsView(CreateAPIView, GenericViewSet):
    """
    View to save a list of events.
    """
    # TODO overwrite create and add async process to save the event
    # TODO Try get the application with a middleware
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = []
    use_case = EventUseCase

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        try:
            self.use_case().save(
                serializer.validated_data,
                self.request.headers.get("Application"),
            )
        except AplicationNotFoundUseCase as err:
            raise UntrustedApplicationApiError()
        except CategoryNotFoundUseCase as err:
            raise CategoryNotFoundApiError()
        except CategoryWithoutStandardUseCase as err:
            raise CategoryWithoutStandardApiError()

        return Response([], status=status.HTTP_201_CREATED)
