from django.urls import path
from .views import *

urlpatterns = [
    path('write/<str:username>', write_message, name="write_message"),
    path('send/<str:username>', send_message, name="send_message"),
    path('received/', received_list, name="received_list"),
]
