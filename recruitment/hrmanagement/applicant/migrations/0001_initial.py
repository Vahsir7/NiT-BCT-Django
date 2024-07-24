# Generated by Django 5.0.7 on 2024-07-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Applicants",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("mobile", models.CharField(max_length=20)),
                ("uimage", models.TextField()),
            ],
            options={
                "db_table": "tbl_applicant",
            },
        ),
    ]
