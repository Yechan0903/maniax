from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from main.models import CustomUser
from django.utils import timezone
from datetime import timedelta

#메세지 작성 화면 보여주기
@login_required
def write_message(request, user_id):
    receiver = get_object_or_404(CustomUser, id=user_id)
    
    today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + timedelta(days=1)

    sent_messages_count = message.objects.filter(
        sender=request.user,
        timestamp__range=(today_start, today_end)
    ).count()
    
    context = {
        'user_id':user_id,
        'receiver':receiver,
        'sent_messages_count': sent_messages_count,
        'limit_reached': sent_messages_count >= 5,
    }
    
    if sent_messages_count < 5:
        return render(request, 'write_message.html', context)
    
    return render(request, 'write_message.html', context)

#메세지 전송하기
@login_required
def send_message(request, user_id):
    receiver = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            new_message = message(
                sender=request.user,
                receiver=receiver,
                content=content,
                timestamp=timezone.now()
            )
            new_message.save()
            return redirect('user_profile', user_id=user_id)
    return redirect('write_message')

#받은 메세지 목록 확인
@login_required
def received_list(request):
    received_messages= message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'received_list.html', {'received_messages':received_messages})

@login_required
def sent_list(request):
    sent_messages= message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'sent_list.html', {'sent_messages':sent_messages})
