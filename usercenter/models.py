from django.db import models
from django.contrib.auth.models import User


class ActivateCode(models.Model):
    owner = models.ForeignKey(User, verbose_name="用户")
    code = models.CharField("激活码", max_length=100)
    expire_timestamp = models.DateTimeField()
    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.code


    class Meta:
        verbose_name = "激活码"
        verbose_name_plural = "激活码"

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sex = models.IntegerField("性别",choices=((0, "男"), (-1, "女")),default=0)
    birthday = models.DateTimeField("生日",null=True, blank=True)
    avatar = models.CharField("头像", max_length=300, blank=True)










