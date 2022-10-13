from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class AmazonProducts(models.Model):
  amazon_link = models.CharField(max_length=1024, null=True, blank=True)
  name = models.CharField(max_length=255, null=True, blank=True)
  my_price = models.CharField(max_length=255, null=True, blank=True)
  amazon_price = models.CharField(max_length=255, null=True, blank=True)
  cost = models.CharField(max_length=255, null=True, blank=True)
  fee = models.CharField(max_length=255, null=True, blank=True)
  stock = models.CharField(max_length=255, null=True, blank=True)
  bought_from = models.CharField(max_length=255, null=True, blank=True)
  image = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return self.name