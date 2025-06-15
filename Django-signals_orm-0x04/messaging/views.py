from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Message

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect('home')

@login_required
def send_message(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    
    if request.method == 'POST':
        content = request.POST.get("content")
        parent_id = request.POST.get("parent_id")
        parent_message = Message.objects.filter(id=parent_id).first() if parent_id else None
        
        Message.objects.create(
            sender = request.user,
            receiver= receiver,
            content=content,
            parent_message=parent_message,
        )
        return redirect('inbox')
    
    return