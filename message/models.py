from django.db import models
from main.models import CustomUser

class message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_message', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_message', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)