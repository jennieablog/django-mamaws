# Generated by Django 3.0.14 on 2022-08-18 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='user',
            new_name='account',
        ),
    ]