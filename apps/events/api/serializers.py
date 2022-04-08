from rest_framework import serializers

from ..models import Event


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "session_id",
            "category",
            "name",
            "data",
            "timestamp",
        ]
