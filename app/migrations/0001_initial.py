# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-19 05:26
from __future__ import unicode_literals

import app.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textFile', models.FileField(storage=app.storage.OverwriteStorage(), upload_to='texts/')),
            ],
        ),
    ]
