# Generated by Django 4.1.5 on 2023-01-29 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ClientApp", "0004_stat_user_tel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stat_user",
            name="tel",
            field=models.IntegerField(default="000000000"),
        ),
    ]
