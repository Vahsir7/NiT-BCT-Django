# Generated by Django 5.0.7 on 2024-07-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proj1app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pname", models.CharField(max_length=100)),
                ("desc", models.TextField()),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField()),
            ],
            options={
                "db_table": "products",
            },
        ),
    ]
