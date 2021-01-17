from datetime import datetime
from django.db import models
from apps.orgs.models import org_info,teacher_info

# Create your models here.
class course_info(models.Model):
    image=models.ImageField(upload_to="course/" ,max_length=200,verbose_name="课程封面")
    name=models.CharField(max_length=200,verbose_name="课程名称")
    study_time=models.IntegerField(default=0,verbose_name="学习时长")
    study_num=models.IntegerField(default=0,verbose_name="学习人数")
    level=models.CharField(choices=( ('gj',"高级"),("zj","中级"),("cj","初级")  ),max_length=5,verbose_name="课程难度")
    love_number=models.IntegerField(default=0,verbose_name="收藏数")
    click_number=models.IntegerField(default=0,verbose_name="访问数量")
    desc=models.CharField(max_length=200,verbose_name="课程简介")
    detail=models.TextField(verbose_name="课程详情")
    category=models.CharField(choices=( ("qd","前端"),("hd","后端")  ),default="qd",verbose_name="课程类型")
    course_notice=models.CharField(verbose_name="课程公告",max_length=200)
    course_need=models.CharField(max_length=100,verbose_name="课程须知")
    tercher_tel=models.CharField(max_length=11,verbose_name="讲师教导")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    orgInfo=models.ForeignKey(org_info,verbose_name="所属机构",on_delete=models.CASCADE)
    teacher_info=models.ForeignKey(teacher_info,verbose_name="所属讲师",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="课程信息"
        verbose_name_plural=verbose_name
class lesson_info(models.Model):
    name=models.CharField(max_length=50,verbose_name="章节名称")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    courseInfo=models.ForeignKey(course_info,verbose_name="所属课程",on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="章节信息"
        verbose_name_plural=verbose_name
class viedo_info(models.Model):
    name=models.CharField(max_length=50,verbose_name="视频名称")
    long=models.IntegerField(default=0,verbose_name="视频时长")
    video_url=models.URLField(default="",verbose_name="视频地址",max_length=200)
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="视频信息"
        verbose_name_plural=verbose_name
class source_info(models.Model):
    name=models.CharField(max_length=50,verbose_name="资源名称")
    download_url=models.FileField(upload_to="source/",verbose_name="文件下载",max_length=200)
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    courseInfo=models.ForeignKey(course_info,verbose_name="所属课程",on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="资源信息"
        verbose_name_plural=verbose_name










