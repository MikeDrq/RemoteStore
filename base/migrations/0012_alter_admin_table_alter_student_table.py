# Generated by Django 4.1.3 on 2024-04-26 13:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0011_admin"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="admin",
            table="Admin",
        ),
        migrations.AlterModelTable(
            name="student",
            table="Student",
        ),
    ]