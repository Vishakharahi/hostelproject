# Generated by Django 4.1.4 on 2022-12-28 16:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hostel', '0003_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HostelDetails',
            new_name='HostelDetail',
        ),
    ]