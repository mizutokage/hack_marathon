from django.db import models

class Account_info(models.Model):
  account_name = models.CharField(max_length=100)
  memo = models.TextField()
  def __str__(self):
    return self.account_name