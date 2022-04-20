from rest_framework import serializers

from ..models import Event


class EventsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=200)

    class Meta:
        model = Event
        fields = [
            "session_id",
            "category",
            "name",
            "data",
            "timestamp",
        ]
