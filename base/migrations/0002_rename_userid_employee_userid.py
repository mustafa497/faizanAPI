# Generated by Django 3.2.1 on 2021-05-11 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='userID',
            new_name='userid',
        ),
    ]
