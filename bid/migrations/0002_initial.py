# Generated by Django 5.1.2 on 2024-10-21 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bid', '0001_initial'),
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='mobile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='mobile.mobile'),
        ),
    ]