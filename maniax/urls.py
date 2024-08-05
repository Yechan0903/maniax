from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('following_rankings/', views.following_rankings_view, name="following_rankings_view"),
    path('naverocr/', include('naverocr.urls')),
]

urlpatterns += static(
    #MEDIA_URL로 시작하는 URL요청이 오면
    prefix=settings.MEDIA_URL,
    #MEDIA_ROOT에서 파일을 찾아 돌려줌
    documnet_root=settings.MEDIA_ROOT
)