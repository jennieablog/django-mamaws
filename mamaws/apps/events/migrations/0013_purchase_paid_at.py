# Generated by Django 3.0.14 on 2022-08-18 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20220818_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='paid_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
