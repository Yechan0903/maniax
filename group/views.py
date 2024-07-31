from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Group
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import GroupForm
from main.models import ScreenTime
from django.http import HttpResponseForbidden

@login_required
def my_group(request):
    user = request.user
    user_groups = user.user_groups.all().order_by('-created_at')
    
    paginator = Paginator(user_groups, 10)  # 페이지당 10개의 그룹을 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'group/my_group.html', {'page_obj': page_obj})

@login_required
def all_group(request):
    groups = Group.objects.all().order_by('-created_at')
    
    paginator = Paginator(groups, 10)  # 페이지당 10개의 그룹을 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'group/all_group.html', {'page_obj': page_obj})

@login_required
def group_room(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    screen_times = ScreenTime.objects.filter(user__in=group.users.all()).order_by('-total_minutes')
    
    paginator = Paginator(screen_times, 10)  # Show 10 screen times per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'group/group_room.html', context)

@login_required
def create_group(request):
    user = request.user
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.master = user
            group.save()
            group.users.add(user)
            return redirect('group_room', group_id=group.id)
    else:
        form = GroupForm()
    return render(request, 'group/create_group.html', {'form': form})

@login_required
def search_group(request):
    query = request.GET.get('q', '')
    groups = Group.objects.all().order_by('-created_at')  # 최신 생성순으로 정렬

    if query:
        groups = groups.filter(title__startswith=query)

    # Pagination
    paginator = Paginator(groups, 10)  # 한 페이지에 10개 그룹 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'page_obj': page_obj,
    }
    return render(request, 'group/search_group.html', context)

@login_required
def group_setting(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    is_master = request.user == group.master
    
    if request.method == 'POST':
        if is_master:
            form = GroupForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
                return redirect('group_room', group_id=group.id)
        else:
            group.users.remove(request.user)
            return redirect('my_group')
    
    else:
        if is_master:
            form = GroupForm(instance=group)
        else:
            form = None

    return render(request, 'group/group_setting.html', {'form': form, 'group': group, 'is_master': is_master})

@login_required
def kick_out_user(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    user = request.user

    if group.master != user:
        return HttpResponseForbidden("권한이 없습니다.")

    if request.method == 'POST':
        user_id_to_kick = request.POST.get('user_id')
        user_to_kick = group.users.filter(id=user_id_to_kick).first()
        if user_to_kick:
            group.users.remove(user_to_kick)
            # Redirect to avoid form resubmission on page refresh
            return redirect('kick_out_user', group_id=group.id)

    users = group.users.exclude(id=user.id)  # Exclude the group master from the list

    context = {
        'group': group,
        'users': users,
    }
    return render(request, 'group/kick_out_user.html', context)

@login_required
def change_group_master(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    user = request.user

    if group.master != user:
        return HttpResponseForbidden("권한이 없습니다.")

    if request.method == 'POST':
        new_master_id = request.POST.get('new_master')
        new_master = group.users.filter(id=new_master_id).first()
        if new_master:
            group.master = new_master
            group.save()
            # Redirect to avoid form resubmission on page refresh
            return redirect('group_room', group_id=group.id)

    users = group.users.exclude(id=user.id)  # Exclude the current master

    context = {
        'group': group,
        'users': users,
    }
    return render(request, 'group/change_group_master.html', context)

@login_required
def remove_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.user != group.master:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        group.delete()
        return redirect('my_group')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Group

@login_required
def account_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    user = request.user

    # Check if the user is already a member of the group
    if group.users.filter(id=user.id).exists():
        is_member = True
    else:
        is_member = False

    if request.method == 'POST' and not is_member:
        password = request.POST.get('password')
        if group.password and group.password != password:
            error_message = "비밀번호가 틀렸습니다."
        else:
            group.users.add(user)
            return redirect('group_room', group_id=group.id)
    else:
        error_message = None

    context = {
        'group': group,
        'is_member': is_member,
        'error_message': error_message,
    }
    return render(request, 'group/account_group.html', context)

