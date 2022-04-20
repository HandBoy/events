import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Application(models.Model):
    name = models.CharField(max_length=200)
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, max_length=100, unique=True, db_index=True
    )


class Category(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)


class Event(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, max_length=100, unique=True, db_index=True
    )
    session_id = models.UUIDField(max_length=100, db_index=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    data = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
