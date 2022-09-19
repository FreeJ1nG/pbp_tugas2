from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class MyWatchList(models.Model):
  watched = models.BooleanField(default=False)
  title = models.CharField(max_length=100)
  rating = models.DecimalField(default=1, decimal_places=2, max_digits=3, validators=[
    MaxValueValidator(5),
    MinValueValidator(1),
  ])
  release_date = models.DateField(default=timezone.now)
  review = models.TextField()

  @property  
  def get_formatted_date(self):
    return self.release_date.strftime("%d %B, %Y")