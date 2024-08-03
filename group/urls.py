from django.urls import path
from . import views

urlpatterns = [
    path('mygroup/', views.my_group, name='my_group'),
    path('allgroup/', views.all_group, name='all_group'),
    path('group/<int:group_id>/', views.group_room, name='group_room'),
    path('search/', views.search_group, name='search_group'),
    path('creategroup/', views.create_group, name='create_group'),  # create_group 뷰를 나중에 추가합니다.
    path('accountgroup/<int:group_id>/', views.account_group, name='account_group'),
    path('groupsetting/<int:group_id>/', views.group_setting, name='group_setting'),
    path('kickout/<int:group_id>/', views.kick_out_user, name='kick_out_user'),
    path('changemaster/<int:group_id>/', views.change_group_master, name='change_group_master'),
    path('removegroup/<int:group_id>/', views.remove_group, name='remove_group'),
]
