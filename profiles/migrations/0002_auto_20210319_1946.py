# Generated by Django 3.1.7 on 2021-03-19 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='expire_date_subscription',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_subscribed',
        ),
    ]
