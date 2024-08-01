from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser, ScreenTime
from .forms import ScreenTimeForm, CustomUserCreationForm
from django.contrib.auth.models import User

def rankings_view(request):
    screen_times = ScreenTime.objects.order_by('-total_minutes')
    
    context = {'screen_times': screen_times}
    
    user = request.user
    if request.user.is_authenticated:
        screen_time, created = ScreenTime.objects.get_or_create(user=user)
        if created:
            screen_time.total_minutes = 0
            screen_time.save()
        if request.method == 'POST':
            form = ScreenTimeForm(request.POST, instance=screen_time)
            if form.is_valid():
                form.save()
                ScreenTime.update_rankings()
                return redirect('rankings')
        else:
            form = ScreenTimeForm(instance=screen_time)
        return render(request, 'rankings.html', {'screen_times': screen_times, 'form': form})
        
    return render(request, 'rankings.html', context)

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
