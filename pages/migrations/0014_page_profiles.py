# Generated by Django 3.0.3 on 2020-04-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200427_1208'),
        ('pages', '0013_remove_page_profiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='profiles',
            field=models.ManyToManyField(related_name='profiles', to='registration.Profile'),
        ),
    ]
