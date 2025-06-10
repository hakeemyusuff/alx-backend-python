from rest_framework import permissions
from .models import Message, Conversation

class IsSenderOrReceiver(permissions.BasePermission):
    """Allows access only to users who are sender or receiver of a message.
    """
    
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.receiver == request.user
    

class IsParcticipant(permissions.BasePermission):
    """Allows access to only participants that is part of the conversation.
    """
    
    def has_object_permission(self, request, view, obj):
        return request.user in obj.particpants.all()