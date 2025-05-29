from rest_framework import serializers
from .models import User, Conversation, Message


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        models = Conversation
        fields = ("conversation_id", "participants")


class UserSerializer(serializers.ModelSerializer):
    conversations = ConversationSerializer(many=True)

    class Meta:
        models = User
        fields = (
            "user_id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "conversations",
        )


class MessageSerializer(serializers.ModelSerializer):
    models = Message
    fields = (
        "message_id",
        "message_body",
        "sent_at",
        "created_at",
    )
