# Generated by Django 3.1.7 on 2021-03-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0010_remove_subscription_price_for_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='price_for_day',
            field=models.FloatField(null=True),
        ),
    ]
