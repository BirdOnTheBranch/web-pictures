# Generated by Django 3.0.3 on 2020-07-26 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0015_remove_user_following'),
        ('registration', '0010_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
