# Generated by Django 3.1.7 on 2021-03-19 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='expire_date_subscription',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='is_subscribed',
            field=models.BooleanField(null=True),
        ),
    ]
