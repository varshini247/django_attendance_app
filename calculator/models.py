from django.db import models
from django_mysql.models import ListCharField
from django.contrib.auth.models import User


# Create your models here.

class Day(models.Model):
    # abs_days =  ListCharField(
    #     base_field=models.CharField(max_length=1),
    #     size=11,
    #     max_length=(2* 15) , # 6 * 10 character nominals, plus commas,
    #     null = True
    # )
    uid = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    year = models.DateField(null=True)
    month = models.DateField(null=True)
    abs_days = models.TextField(null=True)

