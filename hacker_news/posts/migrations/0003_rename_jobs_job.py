# Generated by Django 4.0.2 on 2022-02-14 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_jobs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
    ]
