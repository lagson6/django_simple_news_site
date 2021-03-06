# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0005_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts_tags',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='posts_tags',
            name='tag_id',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='users_app.tag'),
        ),
        migrations.DeleteModel(
            name='posts_tags',
        ),
    ]
