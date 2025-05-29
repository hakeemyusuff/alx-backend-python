from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    phone_number = models.CharField(max_length=50)


class Conversation(models.Model):
    Conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    participants = models.ManyToManyField(User, related_name="conversations")


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    message_body = models.TextField()
    sent_at = models.TimeField(auto_now_add=True)
    created_at = models.TimeField(auto_now_add=True)
