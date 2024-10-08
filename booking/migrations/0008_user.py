# Generated by Django 4.2.11 on 2024-09-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0007_alter_booking_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
