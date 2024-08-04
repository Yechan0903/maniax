from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ScreenTimeForm, CustomUserCreationForm
from django.contrib.auth.models import User
from relationship.models import Relationship
from django.core.paginator import Paginator

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
        following_user_ids = Relationship.objects.filter(from_user=user).values_list('to_user_id')
        following_screen_times = ScreenTime.objects.filter(user__id__in=following_user_ids).order_by('-total_minutes')
        return render(request, 'rankings.html', {'screen_times': screen_times, 'form': form, 'following_screen_times':following_screen_times,})
        
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


@login_required
def following_rankings_view(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    following_user_ids = Relationship.objects.filter(from_user=user).values_list('to_user_id')
    following_screen_times = ScreenTime.objects.filter(user__id__in=following_user_ids).order_by('-total_minutes')
    context = {
        'user':user,
        'following_screen_times':following_screen_times,
    }
    return render(request, 'following_rankings.html', context)

def search_user(request):
    query = request.GET.get('q', '')
    users = CustomUser.objects.all().order_by('-date_joined')  # 최신 생성순으로 정렬

    if query:
        users = users.filter(username__startswith=query)

    # Pagination
    paginator = Paginator(users, 10)  # 한 페이지에 10개 그룹 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'page_obj': page_obj,
    }
    return render(request, 'search_user.html', context)

@login_required
def myinfo_account(request):
    # 나중에 추가합니다.
    return render(request, 'myinfo_account.html')

@login_required
def myinfo_alert(request):
    # 나중에 추가합니다.
    return render(request, 'myinfo_alert.html')

@login_required
def myinfo_appinfo(request):
    # 나중에 추가합니다.
    return render(request, 'myinfo_appinfo.html')

@login_required
def myinfo_calender(request):
    # 나중에 추가합니다.
    return render(request, 'myinfo_calender.html')

@login_required
def myinfo_customerSupport(request):
    # 나중에 추가합니다.
    return render(request, 'myinfo_customerSupport.html')

@login_required
def myinfo_help(request):
    # 나중에 추가합니다.
    return render(request, 'myinfo_help.html')

@login_required
def myinfo_notice(request):
    # 나중에 추가합니다.
    return render(request, 'myinfo_notice.html')

@login_required
def myinfo_setting(request):
    # 나중에 추가합니다.
    return render(request, 'myinfo_setting.html')