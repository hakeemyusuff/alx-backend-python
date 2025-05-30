from django.urls import path
from rest_framework_nested.routers import DefaultRouter
from .views import ConversationViewSet, UserViewSet, MessageViewSet

router = DefaultRouter()
router.register(r"conversations", ConversationViewSet, basename="conversations")
router.register(r"messages", MessageViewSet, basename="messages")
router.register(r"users", UserViewSet, basename="users")
#api-auth