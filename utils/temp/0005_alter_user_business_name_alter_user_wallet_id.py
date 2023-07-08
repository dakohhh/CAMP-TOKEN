# Generated by Django 4.1.7 on 2023-05-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_remove_user_business_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="business_name",
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="wallet_id",
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
