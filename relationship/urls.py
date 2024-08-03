from django.urls import path
from relationship.views import *

urlpatterns = [
    path('<int:user_id>/profile/', user_profile, name='user_profile'),
    path('<int:user_id>/follow/', follow, name="follow"),
    path('<int:user_id>/followers', followers, name="followers"),
    path('<int:user_id>/following', following, name="following"),
]