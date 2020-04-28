# Generated by Django 3.0.3 on 2020-04-28 17:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0008_auto_20200427_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='users',
            field=models.ManyToManyField(related_name='avatars', to=settings.AUTH_USER_MODEL),
        ),
    ]
