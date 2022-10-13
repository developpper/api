from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class Freestyle(models.Model):
  document_id = models.CharField(max_length=255, null=True, blank=True)
  second_party = models.CharField(max_length=255, null=True, blank=True)
  nationality = models.CharField(max_length=255, null=True, blank=True)
  date = models.CharField(max_length=255, null=True, blank=True)
  occupation = models.CharField(max_length=255, null=True, blank=True)
  paid_amount = models.CharField(max_length=255, null=True, blank=True)
  type = models.CharField(max_length=255, null=True, blank=True)
  manf_year = models.CharField(max_length=255, null=True, blank=True)
  color = models.CharField(max_length=255, null=True, blank=True)
  featured_no = models.CharField(max_length=255, null=True, blank=True)
  body = models.CharField(max_length=255, null=True, blank=True)
  length = models.CharField(max_length=255, null=True, blank=True)
  width = models.CharField(max_length=255, null=True, blank=True)
  depth = models.CharField(max_length=255, null=True, blank=True)
  load = models.CharField(max_length=255, null=True, blank=True)
  no_motor = models.CharField(max_length=255, null=True, blank=True)
  engine_sr = models.CharField(max_length=255, null=True, blank=True)
  engine_type = models.CharField(max_length=255, null=True, blank=True)
  engine_power = models.CharField(max_length=255, null=True, blank=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return self.second_party