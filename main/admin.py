from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class ScreenTimeInline(admin.StackedInline):
    model = ScreenTime
    can_delete = False
    
class CustomUserAdmin(UserAdmin):
    inlines = [
        ScreenTimeInline,
    ]
               
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ScreenTime)


