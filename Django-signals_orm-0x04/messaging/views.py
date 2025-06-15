from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_page

User = get_user_model()


@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect("home")


@login_required
def send_message(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)

    if request.method == "POST":
        content = request.POST.get("content")
        parent_id = request.POST.get("parent_id")
        parent_message = (
            Message.objects.filter(id=parent_id).first() if parent_id else None
        )

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content,
            parent_message=parent_message,
        )
        return redirect("inbox")

    return


def get_threaded_replies(message):
    """Recursively get all replies to a message"""
    replies = []
    direct_replies = message.replies.all().select_related("sender", "receiver")
    for reply in direct_replies:
        replies.append(reply)
        replies.extend(get_threaded_replies(reply))
    return replies

@cache_page(60)
@login_required
def view_thread(request, message_id):
    message = get_object_or_404(
        Message.objects.select_related("sender", "receiver"), id=message_id
    )
    replies = get_threaded_replies(message)
    return


@login_required
def unread_message_view(request):
    unread_messages = Message.unread.unread_for_user(request.user).only(
        "id",
        "content",
        "timestamp",
    )
    return
