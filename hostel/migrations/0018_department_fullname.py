# Generated by Django 4.1.5 on 2023-02-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0017_department_remove_hosteldetail_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='Fullname',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
