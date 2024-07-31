from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ScreenTimeForm, CustomUserCreationForm

def send_message(request, username):
    receiver = get_object_or_404(settings.AUTH_USER_MODEL, username=username)
    if request.method == "POST":
        content = request.POST.get('content')
        message = Message(sender=request.user, receiver=receiver, content=content)
        message.save()
        return redirect('profile', username=username)
    return render(request, 'send_message.html', {'receiver': receiver})

def rankings_view(request):
    screen_times = ScreenTime.objects.order_by('-total_minutes')
    return render(request, 'rankings.html', {'screen_times': screen_times})

@login_required
def myinfo_view(request):
    user = request.user
    screen_time, created = ScreenTime.objects.get_or_create(user=user)
    if created:
        screen_time.total_minutes = 0
        screen_time.save()
    if request.method == 'POST':
        form = ScreenTimeForm(request.POST, instance=screen_time)
        if form.is_valid():
            form.save()
            ScreenTime.update_rankings()
            return redirect('myinfo')
    else:
        form = ScreenTimeForm(instance=screen_time)
    return render(request, 'myinfo.html', {'form': form})

def login_or_signup_view(request):
    return render(request, 'login_or_signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('rankings')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            ScreenTime.objects.create(user=user, total_minutes=0)
            return redirect('myinfo')
        else:
            return render(request, 'signup.html', {'form': form, 'errors': form.errors})
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('rankings')
