# Generated by Django 3.0.14 on 2022-08-18 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_reservation_approval_rejection_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='approval_rejection_notes',
            new_name='remarks',
        ),
    ]
