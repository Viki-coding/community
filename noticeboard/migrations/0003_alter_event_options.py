# Generated by Django 4.2.18 on 2025-02-06 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard', '0002_rename_time_event_starttime_event_excerpt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-created']},
        ),
    ]
