# Generated by Django 4.1.7 on 2023-04-19 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VerificationToken",
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
                ("user_email", models.EmailField(max_length=254)),
                ("token", models.CharField(max_length=64, unique=True)),
                ("expiration_time", models.DateTimeField()),
            ],
        ),
    ]
