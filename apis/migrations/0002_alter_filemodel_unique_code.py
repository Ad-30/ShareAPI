# Generated by Django 4.2.2 on 2023-06-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filemodel",
            name="unique_code",
            field=models.CharField(blank=True, max_length=6),
        ),
    ]