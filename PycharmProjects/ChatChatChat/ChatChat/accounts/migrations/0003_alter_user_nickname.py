# Generated by Django 4.1.9 on 2023-06-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_avatar_user_nickname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="nickname",
            field=models.CharField(max_length=125, unique=True),
        ),
    ]
