from django.db.models import post_save
from django.dispatch import receiver
from .models import Message, Notification

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **keargs):
    if created:
        Notification.objects.create(
            user=instance.receiver, 
            message=instance
        )