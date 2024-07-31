from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from main.models import CustomUser
from django.urls import reverse
from django.http import HttpResponseRedirect


@login_required
def follow(request, user_id):
    user = request.user #로그인한 유저
    target_user = get_object_or_404(CustomUser, id=user_id) #팔로우하려는 유저
    
    #팔로우하려는 유저가 이미 팔로잉중이면 언팔
    if target_user in user.following.all(): 
        user.following.remove(target_user)
    
    #팔로잉중이 아니면 팔로잉
    else:
        user.following.add(target_user)
    
    next_url = request.META.get('HTTP_REFERER', reverse('user_profile', args=[user.id]))
    return HttpResponseRedirect(next_url)

@login_required
def user_profile(request, user_id):
    #보려는 프로필의 사용자
    target_user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'user_profile.html', {'target_user': target_user})