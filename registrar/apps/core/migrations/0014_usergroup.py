# Generated by Django 2.2.13 on 2020-08-07 19:59

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_delete_discoveryprogram'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
            ],
            options={
                'proxy': True,
                'constraints': [],
                'indexes': [],
            },
            bases=('core.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]