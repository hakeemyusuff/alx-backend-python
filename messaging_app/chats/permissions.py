from rest_framework import permissions
from .models import Message, Conversation


class IsSenderOrReceiver(permissions.BasePermission):
    """Allows access only to users who are sender or receiver of a message."""

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.receiver == request.user


class IsParcticipant(permissions.BasePermission):
    """Allows access to only participants that is part of the conversation."""

    def has_object_permission(self, request, view, obj):
        return request.user in obj.particpants.all()


class IsParticipantOfConversation(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        conversation = getattr(obj, "converstation", None)
        User = request.user

        if conversation and User in conversation.participants.all():
            if request.method in ["PUT", "PATCH", "DELETE", "POST", "GET"]:
                return True

        return False
