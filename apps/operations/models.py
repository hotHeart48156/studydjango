from enum import unique

from django.core.checks import messages
from apps.courses.models import course_info
from apps.users.models import UserProfile
from os import name
from django.db import models
from datetime import datetime
# Create your models here.
class user_ask(models.Model):
    name=models.CharField(max_length=30,verbose_name="姓名")
    phone=models.CharField(max_length=11,verbose_name="手机")
    course=models.CharField(max_length=20,verbose_name="课程")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="用户咨询信息"
        verbose_name_plural=verbose_name
class user_love(models.Model):
    lobe_man=models.ForeignKey(UserProfile,verbose_name="收藏用户")
    love_id=models.IntegerField(verbose_name="收藏id")
    love_type=models.CharField(choices=(("1","org"),("2","course"),("3","teacher")  ),verbose_name="收藏类型")
    lobe_status=models.BooleanField(default=False,verbose_name="收藏状态")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="用户收藏信息"
        verbose_name_plural=verbose_name
class user_course(models.Model):
    study_man=models.ForeignKey(UserProfile,verbose_name="学习用户")
    study_course=models.ForeignKey(course_info,verbose_name="学习课程")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="学习时间")

    def __str__(self):
        return self.study_man
    class Meta:
        unique={"study_man","study_course"}
        verbose_name="用户学习课程信息"
        verbose_name_plural=verbose_name
class user_comment(models.Model):
    comment_man=models.ForeignKey(UserProfile,verbose_name="学习用户")
    comment_course=models.ForeignKey(course_info,verbose_name="学习课程")
    comment_content=models.CharField(max_length=300,verbose_name="评论内容")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="学习时间")
    def __str__(self):
        return self.study_man
    class Meta:
        verbose_name="用户评论课程信息"
        verbose_name_plural=verbose_name
class user_message(models.Model):
    messages_man=models.IntegerField(default=0,verbose_name="消息用户")
    messages_content=models.CharField(max_length=200,verbose_name="消息内容")
    messages_status=models.BooleanField(default=False,verbose_name="课程状态")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="学习时间")
    def __str__(self):
        return self.study_man
    class Meta:
        verbose_name="用户消息信息"
        verbose_name_plural=verbose_name



