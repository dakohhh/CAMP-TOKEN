# Generated by Django 4.1.7 on 2023-05-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_business_name_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]