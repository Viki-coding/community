# Generated by Django 4.2.18 on 2025-02-06 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard', '0003_alter_event_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Main Hall', 'Main Hall'), ('Astroturf', 'Astroturf'), ('Kitchen', 'Kitchen'), ('Meeting Room', 'Meeting Room'), ('Pitch', 'Pitch'), ('Mezzanine', 'Mezzanine')], max_length=50, unique=True)),
            ],
        ),
    ]
