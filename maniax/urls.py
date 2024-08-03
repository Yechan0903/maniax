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
    path('login_or_signup/', views.login_or_signup_view, name='login_or_signup'),
    path('relationship/', include("relationship.urls")),
    path('message/', include('message.urls')),
    path('group/', include('group.urls')),
    path('following_rankings/', views.following_rankings_view, name="following_rankings_view")
]
