# Generated by Django 4.1.7 on 2023-03-29 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_customuser_business_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="wallet_id",
            field=models.IntegerField(default=4303325680, unique=True),
        ),
    ]
