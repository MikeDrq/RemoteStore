# Generated by Django 5.0 on 2024-04-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0013_notification"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="notification_id",
            field=models.CharField(max_length=32),
        ),
    ]
