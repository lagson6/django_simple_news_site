# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 06:25
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('content', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('tag_name', models.CharField(max_length=100)),
                ('tag_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('posts', models.ManyToManyField(to='users_app.post')),
            ],
            options={
                'ordering': ('tag_name',),
            },
        ),
        migrations.AddField(
            model_name='categories',
            name='category',
            field=models.ManyToManyField(to='users_app.post'),
        ),
    ]
