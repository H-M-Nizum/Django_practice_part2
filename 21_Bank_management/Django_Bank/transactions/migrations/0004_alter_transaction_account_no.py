# Generated by Django 4.2.7 on 2023-12-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_transaction_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account_no',
            field=models.IntegerField(default=0),
        ),
    ]