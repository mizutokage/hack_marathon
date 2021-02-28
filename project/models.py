from django.db import models

class Account_info(models.Model):
  account_name = "a"
  account_name = models.CharField(max_length=100)
  category = models.CharField(max_length=100,default='')
  comment = models.TextField()
  slack_ID = models.CharField(max_length=40,default='')
  twitter_ID = models.CharField(max_length=40,default='')
  univercity = models.CharField(max_length=100,default='')
  def __str__(self):
    return self.account_name