# Generated by Django 5.1.2 on 2024-10-24 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0003_rename_mobile_company_mobile_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
