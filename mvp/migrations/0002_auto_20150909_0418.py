# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mvp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(default='no content'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
