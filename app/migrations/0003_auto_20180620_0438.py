# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-20 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180619_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='voice_type',
            field=models.CharField(choices=[('nl-NL-Standard-A', 'nl-NL-Standard-A'), ('en-AU-Standard-A', 'en-AU-Standard-A'), ('en-AU-Standard-B', 'en-AU-Standard-B'), ('en-AU-Standard-C', 'en-AU-Standard-C'), ('en-AU-Standard-D', 'en-AU-Standard-D'), ('en-GB-Standard-A', 'en-GB-Standard-A'), ('en-GB-Standard-B', 'en-GB-Standard-B'), ('en-GB-Standard-C', 'en-GB-Standard-C'), ('en-GB-Standard-D', 'en-GB-Standard-D'), ('en-US-Wavenet-A', 'en-US-Wavenet-A'), ('en-US-Wavenet-B', 'en-US-Wavenet-B'), ('en-US-Wavenet-C', 'en-US-Wavenet-C'), ('en-US-Wavenet-D', 'en-US-Wavenet-D'), ('en-US-Wavenet-E', 'en-US-Wavenet-E'), ('en-US-Wavenet-F', 'en-US-Wavenet-F'), ('en-US-Standard-B', 'en-US-Standard-B'), ('en-US-Standard-C', 'en-US-Standard-C'), ('en-US-Standard-D', 'en-US-Standard-D'), ('en-US-Standard-E', 'en-US-Standard-E'), ('fr-FR-Standard-C', 'fr-FR-Standard-C'), ('fr-FR-Standard-D', 'fr-FR-Standard-D'), ('fr-CA-Standard-A', 'fr-CA-Standard-A'), ('fr-CA-Standard-B', 'fr-CA-Standard-B'), ('fr-CA-Standard-C', 'fr-CA-Standard-C'), ('fr-CA-Standard-D', 'fr-CA-Standard-D'), ('de-DE-Standard-A', 'de-DE-Standard-A'), ('de-DE-Standard-B', 'de-DE-Standard-B'), ('it-IT-Standard-A', 'it-IT-Standard-A'), ('ja-JP-Standard-A', 'ja-JP-Standard-A'), ('ko-KR-Standard-A', 'ko-KR-Standard-A'), ('pt-BR-Standard-A', 'pt-BR-Standard-A'), ('es-ES-Standard-A', 'es-ES-Standard-A'), ('sv-SE-Standard-A', 'sv-SE-Standard-A'), ('tr-TR-Standard-A', 'tr-TR-Standard-A')], default='', max_length=100),
        ),
    ]
