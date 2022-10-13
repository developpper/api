from django.db import models
from django.contrib.auth.models import User



class Base_Company(models.Model):
    company_name = models.CharField(max_length=255, null=True, blank=True)
    address_line_1 = models.CharField(max_length=255, null=True, blank=True) 
    address_line_2 = models.CharField(max_length=255, null=True, blank=True) 
    website = models.CharField(max_length=255, null=True, blank=True)
    base_username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    base_url = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.company_name



# Create your models here.
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(max_length=255, null=True, blank=True)
  mobile = models.CharField(max_length=255, null=True, blank=True)
  base_company = models.ForeignKey(Base_Company, on_delete=models.PROTECT)
  # signature = models.ImageField(upload_to="img", height_field=None, width_field=None, max_length=100)

def __str__(self):
       return str(self.user)


class E_Customer(models.Model):
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    base_company = models.CharField(max_length=255, null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.customer_name