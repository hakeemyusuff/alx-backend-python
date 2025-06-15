from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_messages",
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return f"from {self.sender.first_name} to {self.receiver.first_name} at {self.timestamp}"


class Notification(models.Model):
    user = models.ForeignKey(
        User,
        related_name="notification",
        on_delete=models.CASCADE,
    )
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user} about {self.message.id}"


class MessageHistory(models.Model):
    message = models.ForeignKey(
        Message,
        related_name="history",
        on_delete=models.CASCADE,
    )
    old_content = models.TextField()
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    edited_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"History for message {self.message.id} at {self.edited_at}"
    
