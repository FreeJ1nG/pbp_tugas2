from audioop import reverse
from django.utils import timezone
from django.db import models
import uuid

# Create your models here.
class Item(models.Model):
  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
  name = models.CharField(max_length=50)
  price = models.IntegerField()
  description = models.TextField()
  pub_date = models.DateField(default=timezone.now)
  image = models.ImageField(upload_to="images", null=True, blank=True)
  
  @property
  def get_price_in_rupiah(self):
    p_str = str(self.price)
    p_str = p_str[::-1]
    return '.'.join(p_str[i:i+3] for i in range(0, len(p_str), 3))[::-1]


class CartItem(models.Model):
  item = models.OneToOneField(Item, on_delete=models.CASCADE)
  count = models.IntegerField()
  
  
class Cart(models.Model):
  items = models.ManyToManyField(CartItem)