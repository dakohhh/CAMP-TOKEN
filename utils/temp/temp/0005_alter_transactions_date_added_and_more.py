# Generated by Django 4.1.7 on 2023-07-08 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transaction", "0004_alter_transactions_transaction_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="date_added",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="initiated_by_student",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="was_refunded",
            field=models.BooleanField(default=True),
        ),
    ]
