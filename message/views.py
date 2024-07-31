from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import message
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

#메세지 작성 화면 보여주기
def write_message(request, username):
    return render(request, 'write_message.html', {'username':username})

#메세지 전송하기
def send_message(request, username):
    receiver = get_object_or_404(User, username=username)
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
            return redirect('received_list')
    return redirect('write_message')

#받은 메세지 목록 확인
def received_list(request):
    received_messages= message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'received_list.html', {'received_messages':received_messages})

