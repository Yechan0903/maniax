"""
URL configuration for maniax project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.rankings_view, name='rankings'),
    path('myinfo/', views.myinfo_view, name='myinfo'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('search_user/', views.search_user, name='search_user'),
    path('login_or_signup/', views.login_or_signup_view, name='login_or_signup'),
    path('group/', include('group.urls')),
    path('message/', include('message.urls')),
    path('relationship/', include("relationship.urls")),
    path('following_rankings/', views.following_rankings_view, name="following_rankings_view"),
    path('ocr/', include('ocr.urls')),
    
    path('myinfo_account/', views.myinfo_account, name='myinfo_account'),
    path('myinfo_alert/', views.myinfo_alert, name='myinfo_alert'),
    path('myinfo_appinfo/', views.myinfo_appinfo, name='myinfo_appinfo'),
    path('myinfo_calender/', views.myinfo_calender, name='myinfo_calender'),
    path('myinfo_customerSupport/', views.myinfo_customerSupport, name='myinfo_customerSupport'),
    path('myinfo_help/', views.myinfo_help, name='myinfo_help'),
    path('myinfo_notice/', views.myinfo_notice, name='myinfo_notice'),
    path('myinfo_setting/', views.myinfo_setting, name='myinfo_setting'),
]
