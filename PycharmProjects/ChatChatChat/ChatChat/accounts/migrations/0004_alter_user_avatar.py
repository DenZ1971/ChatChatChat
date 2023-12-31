# Generated by Django 4.1.9 on 2023-06-07 15:54

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_user_nickname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                default=accounts.models.get_default_image,
                upload_to=accounts.models.generate_filename,
            ),
        ),
    ]
