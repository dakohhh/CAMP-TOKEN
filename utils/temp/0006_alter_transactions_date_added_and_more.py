# Generated by Django 4.1.7 on 2023-07-08 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transaction", "0005_alter_transactions_date_added_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="date_added",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2023, 7, 8, 8, 51, 13, 932976, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="transactions",
            name="initiated_by_student",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="was_refunded",
            field=models.BooleanField(default=False),
        ),
    ]
