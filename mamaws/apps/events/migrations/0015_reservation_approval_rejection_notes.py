# Generated by Django 3.0.14 on 2022-08-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_purchase_delivered_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='approval_rejection_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]