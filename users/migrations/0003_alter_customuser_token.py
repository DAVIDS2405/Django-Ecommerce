# Generated by Django 5.1.6 on 2025-02-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_check_email_customuser_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='token',
            field=models.TextField(editable=False, max_length=10),
        ),
    ]
