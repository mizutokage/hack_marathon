<<<<<<< HEAD
from django.db import models

# Create your models here.

class Account_info(models.Model):
  account_name = models.CharField(max_length=100)
  memo = models.TextField()
  def __str__(self):
    return self.account_name
=======
from django.db import models

class UserModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
>>>>>>> 7baf0dce4a0ea4a33394292b51bb8f4256b01695
