import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Application(models.Model):
    name = models.CharField(max_length=200)
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, max_length=100, unique=True, db_index=True
    )


class Event(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, max_length=100, unique=True, db_index=True
    )
    session_id = models.UUIDField(
        max_length=100, unique=True, db_index=True
    )
    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
    )
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    data = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
