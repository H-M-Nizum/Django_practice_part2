# Generated by Django 4.2.7 on 2023-12-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='account_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
