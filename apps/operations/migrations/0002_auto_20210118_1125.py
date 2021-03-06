# Generated by Django 3.1.4 on 2021-01-18 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_love',
            name='love_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='收藏用户'),
        ),
        migrations.AddField(
            model_name='user_course',
            name='study_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course_info', verbose_name='学习课程'),
        ),
        migrations.AddField(
            model_name='user_course',
            name='study_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学习用户'),
        ),
        migrations.AddField(
            model_name='user_comment',
            name='comment_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course_info', verbose_name='学习课程'),
        ),
        migrations.AddField(
            model_name='user_comment',
            name='comment_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学习用户'),
        ),
    ]
