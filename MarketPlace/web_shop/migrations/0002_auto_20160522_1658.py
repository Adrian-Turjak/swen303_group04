# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 04:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=30)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='message_type',
            field=models.CharField(choices=[(b'general', b'Report general issue'), (b'feedback', b'Give us feedback'), (b'refunds', b'Refund and Cancellation'), (b'missing', b'Where is my stuff?'), (b'violation', b'Report violation of Terms of Service'), (b'phishing', b'Report a phishing incident')], default=b'general', max_length=20),
        ),
    ]
