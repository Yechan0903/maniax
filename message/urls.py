from django.urls import path
from .views import *

urlpatterns = [
    path('write/<int:user_id>', write_message, name="write_message"),
    path('send/<int:user_id>', send_message, name="send_message"),
    path('received/', received_list, name="received_list"),
    path('sent/', sent_list, name="sent_list"),
]
