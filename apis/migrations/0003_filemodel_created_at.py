# Generated by Django 4.2.2 on 2023-06-27 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0002_alter_filemodel_unique_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="filemodel",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]