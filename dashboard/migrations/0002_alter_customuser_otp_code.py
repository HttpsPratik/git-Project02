# Generated by Django 5.0.1 on 2024-01-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='otp_code',
            field=models.CharField(blank=True, null=True),
        ),
    ]
