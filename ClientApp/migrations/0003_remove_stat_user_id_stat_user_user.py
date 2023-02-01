# Generated by Django 4.1.5 on 2023-01-27 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ClientApp", "0002_stat_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stat_user",
            name="id",
        ),
        migrations.AddField(
            model_name="stat_user",
            name="user",
            field=models.OneToOneField(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]