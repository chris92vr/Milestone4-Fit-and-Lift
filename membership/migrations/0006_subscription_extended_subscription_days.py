# Generated by Django 3.1.7 on 2021-03-22 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0005_auto_20210320_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='extended_subscription_days',
            field=models.IntegerField(default=30),
        ),
    ]
