# Generated by Django 5.0 on 2024-04-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="admin",
        ),
        migrations.RemoveField(
            model_name="order",
            name="order_person_role",
        ),
        migrations.RemoveField(
            model_name="order",
            name="student",
        ),
        migrations.AddField(
            model_name="order",
            name="name",
            field=models.CharField(default="123", max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="user_id",
            field=models.CharField(default="123", max_length=64),
            preserve_default=False,
        ),
    ]