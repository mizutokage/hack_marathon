from django.db import models

class Account_info(models.Model):
  account_name = "a"
  account_name = models.CharField(max_length=100)
  category = models.CharField(max_length=100,default='')
  memo = models.TextField()
  slack_ID = models.CharField(max_length=40,default='')
  other_ID = models.TextField(default='')
  univercity = models.CharField(max_length=100,default='')
  def __str__(self):
    return self.account_name