# Generated by Django 4.1.4 on 2023-02-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0026_sturoom'),
    ]

    operations = [
        migrations.CreateModel(
            name='W',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STUNAME', models.CharField(max_length=100)),
                ('ROOMNO', models.CharField(max_length=100)),
                ('BEDNO', models.CharField(max_length=100)),
                ('MEMBERS', models.CharField(max_length=100)),
                ('TABLE', models.CharField(max_length=100)),
                ('CHAIR', models.CharField(max_length=100)),
                ('CUPBOARD', models.CharField(max_length=100)),
            ],
        ),
    ]
