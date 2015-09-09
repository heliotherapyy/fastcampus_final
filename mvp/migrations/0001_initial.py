# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('image_file', models.ImageField(upload_to='%Y/%m/%d/')),
                ('likes', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='like_users')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='photo_owner')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(to='mvp.Photo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comment_owner'),
        ),
    ]
