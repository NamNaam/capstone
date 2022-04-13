from django.db import models
from django.contrib.auth.models import User

class TempScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avg_score = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField()
