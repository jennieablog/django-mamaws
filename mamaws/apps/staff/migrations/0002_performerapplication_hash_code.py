# Generated by Django 3.0.14 on 2022-08-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='performerapplication',
            name='hash_code',
            field=models.CharField(default=12345678, max_length=8),
            preserve_default=False,
        ),
    ]
