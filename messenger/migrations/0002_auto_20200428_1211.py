# Generated by Django 3.0.3 on 2020-04-28 10:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Threat',
            new_name='Thread',
        ),
    ]
