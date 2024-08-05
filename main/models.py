from django.contrib.auth.models import AbstractUser
from django.db import models
from relationship.models import Relationship

class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        "self", #User 인스턴스가 다른 인스턴스 참조
        verbose_name="팔로우 중인 사용자들",
        related_name="followers",
        symmetrical=False,
        through="relationship.Relationship"
    )
    top_apps = models.JSONField(default=dict, blank=True, null=True)
    total_screentimes = models.IntegerField(blank=True, null=True)
    
class ScreenTime(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='screen_time')
    total_minutes = models.PositiveIntegerField(default=0)  # 스크린 타임 총 분

    def __str__(self):
        hours = self.total_minutes // 60
        minutes = self.total_minutes % 60
        return f"{self.user.username} - {hours} hours {minutes} minutes"

    @staticmethod
    def update_rankings():
        screen_times = ScreenTime.objects.order_by('-total_minutes')
        for idx, screen_time in enumerate(screen_times, start=1):
            screen_time.rank = idx
            screen_time.save()

    rank = models.PositiveIntegerField(default=0)  # 랭킹
