from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.models import CustomUser
 
class FollowersInline(admin.TabularInline):
    model = CustomUser.following.through
    fk_name = "from_user"
    verbose_name= "내가 팔로우하고 있는 사용자"
    verbose_name_plural = f"{verbose_name} 목록"
    extra = 1
    
class FollowingInline(admin.TabularInline):
    model = CustomUser.following.through
    fk_name = "to_user"
    verbose_name= "나를 팔로우하고 있는 사용자"
    verbose_name_plural = f"{verbose_name} 목록"
    extra = 1

class CustomUserAdmin(UserAdmin):
    inlines = [
        FollowersInline,
        FollowingInline,
    ]
               



