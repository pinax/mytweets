# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.IntegerField()),
                ('in_reply_to_status_id', models.IntegerField(blank=True, null=True)),
                ('in_reply_to_user_id', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField()),
                ('source', models.TextField()),
                ('text', models.TextField()),
                ('retweeted_status_id', models.IntegerField(blank=True, null=True)),
                ('retweeted_status_user_id', models.IntegerField(blank=True, null=True)),
                ('retweeted_status_timestamp', models.DateTimeField(blank=True, null=True)),
                ('expanded_urls', models.TextField(blank=True)),
            ],
        ),
    ]
