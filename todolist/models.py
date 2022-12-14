from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Task(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField("Date created", default=timezone.now)
  title = models.CharField(max_length=50)
  description = models.TextField()
  is_finished = models.BooleanField(default=False)
  