from typing import List

from apps.events.exceptions import (
    AplicationNotFoundUseCase,
    CategoryNotFoundUseCase,
    CategoryWithoutStandardUseCase,
)

from .models import Application, Category, Event


class EventUseCase:
    def save(self, events_raw: List[dict], application_id: str):
        application = self.get_application(application_id)
        events = []
        
        for event in events_raw:
            category = self.get_category(event.get("category"))

            events.append(
                Event(
                    session_id=event.get("session_id"),
                    application=application,
                    category=category,
                    name=event.get("name"),
                    data=event.get("data"),
                    timestamp=event.get("timestamp"),
                )
            )

        Event.objects.bulk_create(events)
    
    def get_application(self, application_id: str):
        try:
            return Application.objects.get(uuid=application_id)
        except Application.DoesNotExist as err:
            raise AplicationNotFoundUseCase()
    
    def get_category(self, event_category: str):        
        try:
            category = event_category.split()[0]
            name = event_category.split()[1]
            return Category.objects.get(name=name, category=category)
        except Category.DoesNotExist as err:
            raise CategoryNotFoundUseCase()
        except IndexError as err:
            raise CategoryWithoutStandardUseCase()
            