# Generated by Django 3.1.7 on 2021-03-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_auto_20210322_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='price_for_day',
            field=models.FloatField(default=2.5, null=True),
        ),
    ]
