from django.db import models
from django.conf import settings

class Group(models.Model):
    title = models.CharField(max_length=100)
    goals = models.IntegerField(default=0, help_text='목표 시간을 분 단위로 입력해주세요')
    master = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mastered_groups', on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_groups')
    password = models.CharField(max_length=128, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.password:
            self.is_private = True
        else:
            self.is_private = False
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
