# Generated by Django 3.0.14 on 2022-08-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_reservation_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='party_address',
            field=models.CharField(default='test address', max_length=200),
            preserve_default=False,
        ),
    ]
