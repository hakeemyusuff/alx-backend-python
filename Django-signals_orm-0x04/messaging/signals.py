from django.db.models.signals import post_save, pre_save,post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **keargs):
    if created:
        Notification.objects.create(
            user=instance.receiver, 
            message=instance,
        )
        
@receiver(pre_save, sender=Message)
def create_message_history(sender, instance, **kwargs):
    if instance.id:
        try:
            old_msg = Message.objects.get(id=instance.id)
            if old_msg.content != instance.content:
                MessageHistory.objects.create(
                    message=old_msg,
                    old_content=old_msg.content,
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass
        
@receiver(post_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    
    Notification.objects.filter(user=instance).delete()
    
    MessageHistory.objects.filter(message__sender=instance).delete()
    